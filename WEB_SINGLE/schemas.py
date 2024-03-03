from pydantic import BaseModel

class PredictionRequest(BaseModel):
    features: list
    # input data

class PredictionResponse(BaseModel):
    id: int
    result: int