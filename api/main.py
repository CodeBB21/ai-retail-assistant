from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from api.schema import InputData
from api.utils import model

app = FastAPI(title="ML Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(input_data: InputData):
    df = pd.DataFrame([input_data.dict()])
    pred = model.predict(df)[0]
    return {"prediction": float(pred)}
