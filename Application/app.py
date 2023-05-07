import os
import json
import urllib
#import h5py
import torch
import mysql.connector
import pickle as pk
import numpy as np

from keras.models import Sequential, load_model
#from flask_bootstrap import Bootstrap
from os.path import join, dirname, realpath
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash, Response
from werkzeug.utils import secure_filename

import engine # remember to reinclude this

# A <form> tag is marked with enctype=multipart/form-data and an <input type=file> is placed in that form.
# The application accesses the file from the files dictionary on the request object.
# use the save() method of the file to save the file permanently somewhere on the filesystem.

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/') # where uploaded files are stored
ALLOWED_EXTENSIONS = set(['png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF']) # models support png and gif as well

app = Flask(__name__)
#Bootstrap(app)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # max upload - 10MB
app.secret_key = 'secret'



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

# check if an extension is valid and that uploads the file and redirects the user to the URL for the uploaded file
def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def home():
	return render_template('index.html', result=None)


@app.route('/assessment')
def assess():
	return render_template('index.html', result=None, scroll='third')


@app.route('/<a>')
def available(a):
	flash('{} coming soon!'.format(a))
	return render_template('index.html', result=None, scroll='third')



@app.route('/assessment', methods=['GET', 'POST'])
def upload_and_classify():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(url_for('assess'))
		
		file = request.files['file']

		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(url_for('assess'))

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename) # used to secure a filename before storing it directly on the filesystem
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			# return redirect(url_for('uploaded_file',
			#                         filename=filename))
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			model_results = engine.engine(filepath)
			#model_report = engine.predict(filepath)

			return render_template('results.html', result=model_results, scroll='third', filename=filename)
	
	flash('Invalid file format - please try your upload again.')
	return redirect(url_for('assess'))

# @app.route('/show/<filename>')
# def uploaded_file(filename):
#     return render_template('template.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Now one last thing is missing: the serving of the uploaded files. 
# In the upload_file() we redirect the user to url_for('uploaded_file', filename=filename), 
# that is, /uploads/filename. So we write the uploaded_file() function to return the file of that name. 

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],
							   filename)

"Utilisation de ChatGPT-3 pour générer un résumé d'accident à envoyer aux services d'assistance de l'assurance."

"""openai.api_key = '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'
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt="Générez un rapport d'accident détaillé d'une voiture de bonne qualité afin de l'envoyer aux services d'assurance. Ce rapport doit contenir les informations suivantes : le modèle de la voiture (Dacia), la validation des dommages (oui), l'emplacement de l'accident, la gravité (modérée), le coût total estimé des réparations (2000 €). Veuillez également inclure la date et l'heure actuelles.",
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7
)

reply = response.choices[0].text.strip()"""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False) # remember to set back to False	