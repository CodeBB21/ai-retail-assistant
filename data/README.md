📊 Dataset client retail

Ce dossier contient :

customers.csv : dataset utilisé pour l'analyse et l'entraînement

README.md : documentation

📌 Description du dataset

Chaque ligne correspond à un client avec :

Variable	Description
customer_id	Identifiant unique client
age	Âge du client
gender	Sexe (Male/Female)
income	Revenu annuel
city	Ville du client
category	Catégorie d’achat principale
amount	Montant total dépensé
frequency	Nombre d’achats
last_purchase_days_ago	Nombre de jours depuis le dernier achat
churn (optionnel)	Variable présente avant construction target
🎯 Target utilisée pour le modèle

La variable cible a été créée à partir de :

target = (last_purchase_days_ago < 60).astype(int)


➡ 1 = client actif
➡ 0 = client inactif

🚀 Usage du dataset

EDA dans le notebook

Préparation du pipeline ML

Entraînement du modèle final

Déploiement via API FastAPI