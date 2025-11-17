📌 AI Retail Assistant — Churn Prediction API (FastAPI + Docker)

Ce projet est une application complète de Machine Learning qui prédit le comportement client dans un contexte retail.
Elle inclut :

un modèle ML (Random Forest + pipeline sklearn),

une API FastAPI déployée dans Docker,

un frontend simple en HTML/CSS/JS permettant d'effectuer des prédictions en direct,

un pipeline propre : preprocessing → modèle → API → interface utilisateur.

🚀 Fonctionnalités

✔ Prédiction du statut client (0 = inactif / 1 = actif)
✔ Pipeline ML complet (imputation, encodage, scaling, modèle)
✔ API FastAPI prête pour la production
✔ Conteneurisation Docker + déploiement cloud possible
✔ Frontend simple permettant des prédictions en direct
✔ CORS configuré pour communication front ↔ back
✔ Code structuré comme un vrai projet MLOps

🧠 Architecture du projet
project/
│── api/                  # Code FastAPI
│     ├── main.py         # API + endpoints
│     ├── schema.py       # Pydantic schema (JSON input)
│     └── utils.py        # Chargement du modèle
│
│── data/                 # Dataset et documentation
│     ├── customers.csv
│     └── README.md
│
│── frontend/             # Interface utilisateur HTML
│     ├── index.html
│     ├── script.js
│     └── style.css
│
│── model/                # Modèle sauvegardé (pipeline sklearn)
│     └── model.pkl
│
│── notebooks/            # Explorations, entraînement, EDA
│     ├── EDA.ipynb
│     └── README.md
│
│── Dockerfile            # Conteneurisation
│── requirements.txt      # Dépendances
│── generate_dataset.py   # Script de génération de données
└── README.md             # Document actuel

🛠️ Installation & Exécution
1. Cloner le projet
git clone <repo>
cd ai-retail-assistant

2. Construire l’image Docker
docker build -t ml_api .

3. Exécuter l’API
docker run -p 8000:8000 ml_api


API accessible ici :
👉 http://localhost:8000/docs

4. Lancer le frontend (option 1)
cd frontend
python -m http.server 5500


Interface accessible ici :
👉 http://localhost:5500

📡 Déploiement Cloud (Render)

Le projet est prêt pour un déploiement Docker sur :

Render

Railway

Google Cloud Run (recommandé pour production)

Le frontend peut ensuite pointer vers :

https://votre-api.onrender.com/predict

🤖 Modèle Machine Learning
Target utilisée :
target = (last_purchase_days_ago < 60).astype(int)

Colonnes d’entrée :

Numériques :

age

income

amount

frequency

last_purchase_days_ago

Catégorielles :

gender

city

category

Modèle utilisé :
✔ RandomForestClassifier
✔ Pipeline sklearn complet (impute, encode, scale)

Enregistrement :

joblib.dump(rf_model, "model/model.pkl")

✨ Auteur

Projet développé par CodeBB21