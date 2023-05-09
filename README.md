# ECG Machine Learning Model
## Description
Le projet consiste à former un modèle de Machine Learning capable de déterminer (prédire) la classe (normal ou anormal) d'un électrocardiogramme. Et une application intégrant ce modèle capable de prédire (classifier) de nouvelles données.
---
Le jeu de données utilisé est issu de la plateforme [OpenML](https://www.openml.org/search?type=data&status=active&sort=runs&id=44793).
Cet ensemble de données contient les lectures ECG de 4998 patients. Chaque ligne correspond à un seul électrocardiogramme complet d'un patient. Chaque ECG (ligne) est composé de 140 points de données (lectures) et d’une colonne étiquette (1 si l’ECG est normal ou 0 si non).
---
Description des colonnes :
- Les colonnes 0 à 139 (nommés : col_0, col_1, col_2, …, col139) contiennent le point de données ECG pour un patient particulier. Ce sont des nombres à virgule flottante.
- La colonne (col_140) étiquette qui indique si l'ECG est normal ou anormal. C'est une variable catégorielle dont la valeur est soit 0 soit 1. C’est la variable cible (c’est-à-dire la variable à prédire)
---
## Structure du projet
**_Le répertoire principal_**
---
ecgML-Model/
>datas : le sous répertoire contenant le jeu de données
---
>ecgML Model.ipyng : le notebook (conception du modèle)

**_Application de prédictions_**
---
Pour l'interprétation de nouvelles données, une application basée sur [le micro framework Flask](https://flask.palletsprojects.com/en/2.3.x/) a été mise en place. Le fichiers sources sont dans le sous répertoire predictions_app. L'exécution de la dernière cellule du notebook sauvegarde le modèle former dans le sous-dossier predictions_app/model du dossier de l'application de prédiction développée à l'aide du micro framework Flask.
---
Le démarrage de l'application de prédictions est relativement simple :
---
_Pour la première exécution :_
- [x] ouvrir l'invide de commande en mode administrateur et se placer dans le repertoire predictions_app
- [x] [créer un environnement virtuel](https://docs.python.org/fr/3/tutorial/venv.html) dans le dossier predictions_app : ../predictions_app **>** python -m venv nom_env
- [x] activer l'environnement virtuel : ../predictions_app **>** nom_env/Scripts/activate
- [x] installer les différents packages nécessaires à l'aide la commande : (nom_env)../predictions_app **>** pip install -r requirements.txt
- [x] exécuter la commande (nom_env)../predictions_app **>** python app.y pour lancer l'application
---
_Pour les prochaines exécutions :_
- [x] activer l'environnement virtuel
- [x] exécuter la commande > python app.py
