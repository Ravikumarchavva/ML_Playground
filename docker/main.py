from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from apis.carprice import predictPrice
import random
import numpy as np
import pandas as pd
# Load environment variables
load_dotenv()

# Access environment variables
BASE_URL = os.getenv("BASE_URL")
NEXTJS_URL = os.getenv("NEXTJS_URL")

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[BASE_URL, NEXTJS_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, Next.js World!"}


class CarPriceRequest(BaseModel):
    carlength: float
    carwidth: float
    horsepower: float
    brandavg: float
    averagempg: float

from apis.carprice import predictPrice
@app.post("/send_carprice")
def send_carprice(request: CarPriceRequest):
    price = predictPrice(
        request.carlength,
        request.carwidth,
        request.horsepower,
        request.brandavg,
        request.averagempg
    )
    # Example logic for calculating price
    return {"price": price}

from apis.churn import predictChurn

class ChurnPredictionRequest(BaseModel):
    MonthlyCharges: float
    TotalCharges: float
    InternetService: str
    tenure: float
    Contract: str

@app.post("/predict_churn")
def predict_churn(request: ChurnPredictionRequest):
    try:
        result = predictChurn(
            request.MonthlyCharges,
            request.TotalCharges,
            request.InternetService,
            request.tenure,
            request.Contract
        )
        if(result==1):
            return {"prediction": "More probable to Churn"}
        else:
            return {"prediction": "Less probable to Churn"} 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

