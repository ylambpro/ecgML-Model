# ECG Machine Learning - Model
Le projet consiste consiste à former une modèle de Machine Learning capable de déterminer (prédire) la classe (normal ou anormal) d'un électrocardiogramme.

Le jeu de données utilisé est issu de la plateforme [OpenML](https://www.openml.org/search?type=data&status=active&sort=runs&id=44793).

Cet ensemble de données contient les lectures ECG de 4998 patients. Chaque ligne correspond à un seul électrocardiogramme complet d'un patient. Chaque ECG (ligne) est composé de 140 points de données (lectures) et d’une colonne étiquette (1 si l’ECG est normal ou 0 si non).

Description des colonnes :
- Les colonnes 0 à 139 (nommés : col_0, col_1, col_2, …, col139) contiennent le point de données ECG pour un patient particulier. Ce sont des nombres à virgule flottante.
- La colonne (col_140) étiquette qui indique si l'ECG est normal ou anormal. C'est une variable catégorielle dont la valeur est soit 0 soit 1. C’est la variable cible (c’est-à-dire la variable à prédire)

Structure du projet.

Formation du modèle

ecgML-Model/
>datas : le sous répertoire contenant le jeu de données
>ecgML Model.ipyng : le notebook (conception du modèle)

Application de prédictions

Pour l'interprétation de nouvelles données, une application basée sur [le micro framework Flask](https://flask.palletsprojects.com/en/2.3.x/) a été mise en place. Le fichiers sources sont dans le sous répertoire predictions_app.

ecgML-Model/predictions_app/
>model : sous répertoire contenant le modèle générer par le notebook.

