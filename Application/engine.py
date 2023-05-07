import os
import json
import urllib

import h5py
import torch
import mysql.connector
import pandas as pd
import numpy as np
import pickle as pk

from keras.applications.vgg16 import VGG16
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import img_to_array , array_to_img,  load_img
from keras.models import Sequential, load_model
from keras.utils.data_utils import get_file
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash, Response


# connexion au base de données
db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="piecedata"
)


# créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
#cur.execute("CREATE DATABASE piecedata")



# Load models and support
#first_gate = VGG16(weights='imagenet')
first_gate = load_model('static/models/Models/vgg19_stage1_fc-0.999.hdf5')
print("First gate loaded")
second_gate = load_model('static/models/Models/vgg19_stage1_all-0.928.hdf5')
print( "Second gate loaded")
location_model = load_model('static/models/Models/vgg19_stage2_fc-0.673.hdf5')
print("Location model loaded")
#severity_model = pickle.load(open('static/models/Models/resnet152_3_epoch98_step790.pkl', 'rb'))
severity_model = load_model('static/models/Models/vgg19_stage3_fc-0.649.hdf5')
print ("Severity model loaded")
with open('static/models/vgg16_cat_list.pk', 'rb') as f:
	cat_list = pk.load(f)
print ("Cat list loaded")

# from Keras GitHub  
CLASS_INDEX = None
CLASS_INDEX_PATH = 'https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json'


def get_predictions(preds, top=5):
	global CLASS_INDEX
	if len(preds.shape) != 2 or preds.shape[1] != 1000:
		raise ValueError('`decode_predictions` expects '
						 'a batch of predictions '
						 '(i.e. a 2D array of shape (samples, 1000)). '
						 'Found array with shape: ' + str(preds.shape))
	if CLASS_INDEX is None:
		fpath = get_file('imagenet_class_index.json',
						 CLASS_INDEX_PATH,
						 cache_subdir='models')
		CLASS_INDEX = json.load(open(fpath))
	l = []
	for pred in preds:
		top_indices = pred.argsort()[-top:][::-1]
		indexes = [tuple(CLASS_INDEX[str(i)]) + (pred[i],) for i in top_indices]
		indexes.sort(key=lambda x: x[2], reverse=True)
		l.append(indexes)
	return l

def prepare_img_224(img_path):
	img = load_img(img_path, target_size=(256, 256))
	x = img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	return x

def car_categories_gate(img_224, model):
	print ("Validating that this is a picture of your car...")
	pred = model.predict(img_224)
	if pred[0][0] <=.5:
		return True 
	else:
		return False
			

def prepare_img_256(img_path):
	img = load_img(img_path, target_size=(256, 256)) # this is a PIL image 
	x = img_to_array(img) # this is a Numpy array with shape (3, 256, 256)
	x = x.reshape((1,) + x.shape)/255
	return x

def car_damage_gate(img_256, model):
	print ("Validating that damage exists...")
	pred = model.predict(img_256)
	if pred[0][0] <=.5:
		return True # print "Validation complete - proceed to location and severity determination"
	else:
		return False
		# print "Are you sure that your car is damaged? Please submit another picture of the damage."
		# print "Hint: Try zooming in/out, using a different angle or different lighting"

def location_assessment(img_256, model):
	print ("Determining location of damage...")
	pred = model.predict(img_256)
	pred_label = np.argmax(pred, axis=1)
	d = {0: 'Front', 1: 'Rear', 2: 'Side'}
	for key in d.keys():
		if pred_label[0] == key:
			return d[key]
	# 		print "Assessment: {} damage to vehicle".format(d[key])
	# print "Location assessment complete."

def severity_assessment(img_256, model):
	print ("Determining severity of damage...")
	pred = model.predict(img_256)
	pred_label = np.argmax(pred, axis=1)
	d = {0: 'Minor', 1: 'Moderate', 2: 'Severe'}
	for key in d.keys():
		if pred_label[0] == key:
			return d[key]
	# 		print "Assessment: {} damage to vehicle".format(d[key])
	# print "Severity assessment complete."


Operation = []


def Operation_(img_path):
    img_224 = prepare_img_224(img_path)

    y = severity_assessment(img_224, severity_model)
   
    if y == 'Moderate' or y == 'Severe' :
        Operation.append('Echange')
    else :
        Operation.append('Dressage')

    return Operation[0]


# load models
def engine(img_path):
    img_224 = prepare_img_224(img_path)
    g1 = car_categories_gate(img_224, first_gate)
	

    if g1 is False:
        result = {'gate1': 'Car validation check: ', 
        'gate1_result': 0, 
        'gate1_message': {0: 'Are you sure this is a picture of your car? Please retry your submission.', 
        1: 'Hint: Try zooming in/out, using a different angle or different lighting'},
        'gate2': None,
        'gate2_result': None,
        'gate2_message': {0: None, 1: None},
        'location': None,
        'severity': None,
        'Dic' : None ,
        'Main d\'œuvre tolerie 1' : None,
        'Main d\'œuvre tolerie 2' : None ,
        'Main d\'œuvre peinture' :  None,
        'TMain' : None ,
        'Produit de pienture' : None ,
        'Total de Fourniture' : None ,
        'Total' : None,
        'Prix' : None,
        'final': 'the damaged part hasn\'t been detected for this car !'}
        return result

    img_256 = prepare_img_256(img_path)
    g2 = car_damage_gate(img_256, second_gate)

    if g2 is False:
        result = {'gate1': 'Car validation check: ', 
        'gate1_result': 1, 
        'gate1_message': {0: None, 1: None},
        'gate2': 'Damage presence check: ',
        'gate2_result': 0,
        'gate2_message': {0: 'Are you sure that your car is damaged? Please retry your submission.',
        1: 'Hint: Try zooming in/out, using a different angle or different lighting.'},
        'location': None,
        'severity': None,
        'Dic' : None ,
        'Main d\'œuvre tolerie 1' : None,
        'Main d\'œuvre tolerie 2' : None ,
        'Main d\'œuvre peinture' :  None,
        'TMain' : None ,
        'Produit de pienture' : None ,
        'Total de Fourniture' : None ,
        'Total' : None,
        'final': 'Damage assessment unsuccessful!'}
        return result

    
    x = location_assessment(img_256, location_model)
    y = severity_assessment(img_256, severity_model)

    #Results of the seconde model 
    imgr = []
    classes = []
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

    ress = []

    imgr.append(img_path)
    results = model(img_path, size=640)
    # results.pandas().xyxy[0].to_json(orient="records")  # JSON img1 predictions

    results = results.pandas().xyxy[0]

    classes.append(results['name'].tolist())

    #print(classes)
    res = []
    res = list(set(tuple(sorted(classe)) for classe in classes))
    res1 = res[0]
    #print(res)
    #print(res1)
    piece = []
    operation = []

    Dic = {}
    result = {}
    result[Dic] : Dic   
    for i in res1:
        piece.append(i.split('_')[0])
        operation.append(Operation_(img_path))
        #print(piece)
        #print(operation)
        Dic = { a : b for a, b in zip(piece, operation)}
        #print("Dictionnaire 0: ")
        #print(dic)

    MT1 = 0
    MP= 0
    PP1= 0
    PP2= 0
    MT2= 0
    TMain = 0
    prix = 0
    est = 0
    PP = 0
    TF = 0
    Total =0

    result = {'gate1': 'Car validation check: ', 
	'gate1_result': 1, 
	'gate1_message': {0: None, 1: None},
	'gate2': 'Damage presence check: ',
	'gate2_result': 1,
	'gate2_message': {0: None, 1: None},
	'location': x,
	'severity': y,
        'Dic' : Dic ,
        'Main d\'œuvre tolerie 1' : MT1,
        'Main d\'œuvre tolerie 2' : MT2 ,
        'Main d\'œuvre peinture' :  MP,
        'TMain' : TMain ,
        'Produit de pienture' : PP ,
        'Total de Fourniture' : TF ,
        'Total' : Total,
        'final': 'Damage assessment unsuccessful!'}


    for p, op in Dic.items():
        if op == 'Echange':
            print(p)

            sqla = """SELECT prix_recuperable FROM `devis_piece`
                                WHERE  `DMC` = %s and `piece` = %s
                                       """
            date = '2015-2019'

            cur.execute(sqla, (date, p))

            ress = cur.fetchall()

            for r in ress:
                #print(type(r[0]))
                #print(p, r, "--" * 40)
                #Dic1 = {a: b for a, b in zip(p, r)}

                Dic1 = {p: r[0]}
                #print(Dic1)

                for i in Dic1.values():
                    prix += i
                    #prix = float(prix)

                print(prix)
                #print(type(prix))

                result = {'gate1': 'Car validation check: ', 
	                        'gate1_result': 1, 
	                        'gate1_message': {0: None, 1: None},
	                        'gate2': 'Damage presence check: ',
	                        'gate2_result': 1,
	                        'gate2_message': {0: None, 1: None},
	                        'location': x,
	                        'severity': y,
                            'Dic' : Dic ,
                            'Dic1' : {p: r[0]} ,
                            'Main d\'œuvre tolerie 1' : MT1,
                            'Main d\'œuvre tolerie 2' : MT2 ,
                            'Main d\'œuvre peinture' :  MP,
                            'TMain' : TMain ,
                            'Produit de pienture' : PP ,
                            'Total de Fourniture' : TF ,
                            'Total' : Total,
                            'final': 'Damage assessment unsuccessful!'}
                #print("Dictionnaire 1: ")

            #for d in Dic1:
             #   print(d[r])
                # {{sum(d[p])}}

            sql1 = """SELECT SUM(C2_MOT*70) FROM `mot_mop`
                     WHERE `Operation_E` = %s 
                    """
            cur.execute(sql1, (p,))
            res1 = cur.fetchall()
            for l1 in res1:
                MT1=str(l1[0] or 0)
                print('MT1 = '+MT1)

            sql2 = """SELECT SUM(C2_MOP*70) FROM `mot_mop`
                        WHERE `Operation_E` = %s 
                    """
            cur.execute(sql2, (p,))
            res2 = cur.fetchall()
            for l2 in res2:
                MP=str(l2[0] or 0)
                print('MP = '+MP)

            sql3 = """SELECT SUM(C2_MET) FROM `peinture`
                        WHERE `Operation` = %s 
                    """
            cur.execute(sql3, (p,))
            res3 = cur.fetchall()
            for l3 in res3:
                PP1 = str(l3[0] or 0)
                print('PP1 = ' + PP1)

        elif op == 'Dressage':
            print(p)

            #sql5 = """UPDATE `peinture` SET C2_MET=0
                                              #  WHERE Operation!=%s
                                            #"""
            sql5 = """SELECT SUM(C2_MET) FROM `peinture`
                                    WHERE `Operation` = %s 
                    """
            cur.execute(sql5, (p,))
            res5 = cur.fetchall()
            for l5 in res5:
                PP2=str(l5[0] or 0)
                #PP2=str(PP2 or 0)
                print('PP2 = ' + PP2)

            sql6 = """SELECT SUM(C2_Endom_Leger*110) FROM `reparation`
                                                WHERE `Operation_D` = %s 
                                """
            cur.execute(sql6, (p,))
            res6 = cur.fetchall()
            for l6 in res6:
                MT2 = str(l6[0] or 0)
                print('MT2 = ' + MT2)

    result['Dic']=Dic
    result['MT1']=MT1
    result['MT2']=MT2
    result['Mp']=MP
    result['TMain']=float(MT1)+float(MT2)+float(MP)
    result['PP']=float(PP1)+float(PP2)
    result['TF'] =float(PP1)+float(PP2)+float(prix)
    result['Prix'] = prix
    result['Total'] =float(PP1)+float(PP2)+float(prix)+float(MT1)+float(MT2)+float(MP)

    print(result)
    return result


#
#
#
#
#