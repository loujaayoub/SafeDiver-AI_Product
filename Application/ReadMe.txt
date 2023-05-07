
Afin de garantir l'existence de tous les packages nécessaires pour l'éxecution de ce projet 
tapez la commande suivante :

         pip install -r requirements.txt

Ce projet suit la structure suivante :

Input : image de la voiture endommagée

model 1 : Car or not car
	Avec une dataset de deux classes ( car , not car) on a effectué une classification binaire avec Les réseaux de neurones de convolution en appliquant l'architecture pre-entrainée VGG19.
	Le résultat de ce modèle est le fichier vgg19_stage1_fc-0.999.hdf5 qu'on a utilisé dans engine.py



model 2 : Damaged or not damaged
	Avec une dataset de deux classes ( damaged , good) on a effectué une classification binaire avec Les réseaux de neurones de convolution en appliquant l'architecture pre-entrainée VGG19.
	Le résultat de ce modèle est le fichier vgg19_stage1_all-0.928.hdf5 qu'on a utilisé dans engine.py



model 3 : Location of the damage
	Avec une dataset de trois classe ( side , front , rear) on a effectué une classification multiclasses avec Les réseaux de neurones de convolution en appliquant l'architecture pre-entrainée VGG19.
	Le résultat de ce modèle est le fichier vgg19_stage2_fc-0.673.hdf5 qu'on a utilisé dans engine.py



model 4 : Severity of the damage
	Avec une dataset de trois classes ( minor , severe , moderate) on a effectué une classification multiclasses avec Les réseaux de neurones de convolution en appliquant l'architecture pre-entrainée VGG19.
	Le résultat de ce modèle est le fichier vgg19_stage3_fc-0.649.hdf5 qu'on a utilisé dans engine.py


model 5 : Pièces endommagées
	Etape 1 : Annotation des images ( presque 1000 images sans augmentation) avec makesense.ia et VOTT
	Etape 2 : Convertir ces annotation en yolo annotations avec RoboFlow
	Etape 3 : Entrainer Yolo sur Les annotations, le résultat de l'entrainement est le modèle best.pt qui détecte les parties endommagées


Aprés la détection de la piece endommagée, On a utilisé la base de données piecedata.sql pour estimer le prix du réparation/échange ceci inclut le prix de la pièce et le prix de la main d'oeuvre et de la peinture etc ....	


Output : Détection des pièces endommagées et estimation des prix de réparation/échange en se basant sur les prix mentionnés dans la base de données -piecedata-


Affichage : 

Après avoir entré l'image , le site affiche deux tableaux :

-le premier tableau affiche les résultats des modèles 1,2,3 et 4.
-le deuxième tableau affiche les résultats du modèle 5 à savoir les pièces endommagées et l'estimation du prix du réparation ou échange associé à chaque pièce.








