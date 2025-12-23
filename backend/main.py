
import random
from fastapi import FastAPI, HTTPException
from schema import CustomerFeatures, PredictRequest, PredictResponse
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()


# app = FastAPI(title="Customer Spending Prediction API")
app = FastAPI(
    title="TTB Customer Scoring API",
    description="API for predicting spend categories based on income and spend ratio.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows the frontend to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, OPTIONS, etc.
    allow_headers=["*"],
)

# create api for predicting spend category
@app.post("/predict", response_model=PredictResponse)
async def predict_spend_category(request: PredictRequest):
    try:
        # Extract features
        income = request.feature.income
        avg_spend = request.feature.avg_monthly_spend
        
        # Calculate Spend Ratio & Classification Logic
        spend_ratio = avg_spend / income
        
        if spend_ratio < 0.10:
            category = "low"
        elif 0.10 <= spend_ratio < 0.30:
            category = "medium"
        else:
            category = "high"
            
        # Generate random confidence score between 0.70 and 0.95
        confidence_score = round(random.uniform(0.70, 0.95), 2)
        
        return {
            "customer_id": request.customer_id,
            "prediction": category,
            "confidence": confidence_score
        }
        
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Income cannot be zero for ratio calculation.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

