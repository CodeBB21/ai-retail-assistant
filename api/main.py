from fastapi import FastAPI
import pandas as pd

from api.schema import InputData
from api.utils import model

app = FastAPI(title="ML Prediction API")

@app.post("/predict")
def predict(input_data: InputData):
    # Convertir input en DataFrame
    df = pd.DataFrame([input_data.dict()])

    # Prédiction avec pipeline complet
    pred = model.predict(df)[0]

    return {"prediction": float(pred)}
