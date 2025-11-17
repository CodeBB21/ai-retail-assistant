🧪 Notebooks d'analyse & entraînement

Ce dossier contient tous les notebooks utilisés pour :

l’exploration préliminaire du dataset,

l’EDA (analyse exploratoire),

la préparation de la target,

la création du pipeline sklearn,

l’entraînement et l’évaluation des modèles,

la génération du modèle final sauvegardé.

📌 Contenu du dossier
1. EDA.ipynb

Inspection globale du dataset

Étude de la distribution des variables

Analyse des corrélations

Nettoyage & preprocessing simple

Construction de la target

Visualisations (histogrammes, boxplots, heatmap)

2. Modèle ML

Dans ce notebook :

✔ Définition des colonnes numériques & catégorielles
✔ Création du ColumnTransformer
✔ Pipelines ML : Logistic Regression, Random Forest, Gradient Boosting
✔ Évaluation via classification_report
✔ Sauvegarde du modèle final :

joblib.dump(rf_model, "../model/model.pkl")

🧠 À quoi servent ces notebooks ?

Ils permettent de :

✔ Documenter la démarche analytique
✔ Permettre la reproductibilité
✔ Tester plusieurs modèles avant déploiement
✔ Comprendre le comportement du pipeline avant API + Docker

🚀 Étape suivante

Le modèle final sauvegardé est ensuite utilisé par l'API FastAPI dans le dossier :

/api/
   main.py
   schema.py
   utils.py
