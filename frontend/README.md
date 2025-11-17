🎨 Frontend – AI Retail Assistant

Ce dossier contient l’interface utilisateur simple permettant d'interagir avec l’API FastAPI du projet AI Retail Assistant.
L’objectif est de fournir une interface intuitive pour envoyer des données client et obtenir immédiatement une prédiction du modèle Machine Learning.

📌 Contenu du dossier
frontend/
│── index.html      # Interface principale
│── script.js       # Appels API & logique dynamique
└── style.css       # Mise en forme et design

🎯 Fonctionnalités

✔ Formulaire simple permettant de saisir :

âge

revenu

montant dépensé

fréquence d’achat

récence du dernier achat

genre

ville

catégorie d’achat

✔ Envoi automatique de la requête à l’API /predict via JavaScript
✔ Affichage immédiat de la prédiction (0 = inactif, 1 = actif)
✔ Design minimaliste, responsive et épuré
✔ Appels cross-origin possibles grâce au CORS configuré dans FastAPI

🚀 Lancer le frontend en local
Option 1 — Serveur Python (recommandé)

Placez-vous dans le dossier :

cd frontend
python -m http.server 5500


Puis ouvrez dans votre navigateur :

👉 http://localhost:5500/

Option 2 — Serveur intégré FastAPI (optionnel)

Vous pouvez aussi monter le frontend depuis main.py :

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


Puis accéder à :

👉 http://localhost:8000/

🌍 Déploiement du frontend

Pour accéder à votre API déployée (Render / Railway / Cloud Run) :

Modifier script.js :

fetch("https://votre-api.onrender.com/predict", { ... })


Ainsi, vous pouvez :
✔ tester depuis votre PC
✔ tester depuis un smartphone
✔ intégrer le front dans un site web externe

🧩 Technologies utilisées

HTML5

CSS3

JavaScript (Fetch API)

FastAPI (backend)

JSON (format d’échange)

✨ Améliorations possibles

Ajouter des animations visuelles sur la prédiction

Coloration dynamique (vert = 0, rouge = 1)

Ajout d’un graphique d’historique

Version mobile optimisée

Ajout d’un loader / spinner