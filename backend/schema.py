
from pydantic import BaseModel, Field
class CustomerFeatures(BaseModel):
    age: int = Field(..., gt=0, description="Age must be a positive integer")
    income: float = Field(..., gt=0, description="Income must be greater than zero")
    avg_monthly_spend: float = Field(..., ge=0)

class PredictRequest(BaseModel):
    customer_id: str
    feature: CustomerFeatures

class PredictResponse(BaseModel):
    customer_id: str
    prediction: str
    confidence: float