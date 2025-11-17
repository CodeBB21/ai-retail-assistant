⚙️ API – AI Retail Assistant (FastAPI)

Ce dossier contient le backend du projet :
✔ une API FastAPI
✔ un pipeline Machine Learning complet (sklearn)
✔ la logique de prédiction
✔ les schémas d'entrée pour validation

Cette API est utilisée par le frontend, mais peut aussi être consommée par n'importe quel client HTTP (Postman, Python, mobile app…).

📌 Contenu du dossier
api/
│── main.py       # FastAPI : routes, CORS, prédiction
│── schema.py     # Modèle Pydantic pour valider les données d'entrée
└── utils.py      # Chargement du pipeline sklearn

🧠 Fonctionnement de l’API
1️⃣ Chargement du pipeline ML

Le modèle RandomForest + preprocessing sklearn est chargé depuis model/model.pkl.

utils.py contient :

model = joblib.load("model/model.pkl")

2️⃣ Validation des données (Pydantic)

schema.py définit un modèle InputData validant la structure JSON reçue :

class InputData(BaseModel):
    age: float
    income: float
    amount: float
    frequency: float
    last_purchase_days_ago: float
    gender: str
    city: str
    category: str

3️⃣ Endpoint /predict

Déclare un endpoint POST :

@app.post("/predict")
def predict(input_data: InputData):


⚙ Convertit le JSON → DataFrame → envoie dans le modèle
⚙ Retourne la prédiction au format JSON

🚀 Lancer l’API en local (Docker)

Construire l’image :

docker build -t ml_api .


Lancer l’API :

docker run -p 8000:8000 ml_api


API disponible ici :

👉 http://localhost:8000/docs
 (Swagger)

🔐 CORS & communication frontend

FastAPI inclut une configuration CORS permettant au frontend (ou un client externe) d'utiliser l’API :

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

🌍 Déploiement cloud

Compatible Render, Railway, GCP, AWS, Azure.
Fonctionne parfaitement en environnement Docker.

Une fois déployée, l’API sera accessible sur une URL du type :

https://ai-retail-api.onrender.com/predict

📡 Tests & exemples
Exemple de requête :
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
            "age": 30,
            "income": 50000,
            "amount": 150,
            "frequency": 2,
            "last_purchase_days_ago": 10,
            "gender": "Male",
            "city": "Paris",
            "category": "Electronics"
         }'

Réponse :
{
  "prediction": 1
}

🔧 Technologies utilisées

Python 3.11

FastAPI

Uvicorn

scikit-learn

pandas

joblib

Docker

✨ Améliorations possibles

Ajouter /predict_proba

Ajouter /health

Ajouter logs & monitoring

Ajouter versioning (/version)

Ajouter authentification par token