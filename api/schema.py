from pydantic import BaseModel

class InputData(BaseModel):
    age: float
    income: float
    amount: float
    frequency: float
    last_purchase_days_ago: float

    gender: str
    city: str
    category: str
