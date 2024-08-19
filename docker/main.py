from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from dotenv import load_dotenv
import os

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

class ChurnPredictionRequest(BaseModel):
    tenure: str
    contract: str
    monthlyCharges: str
    internetService: str
    paymentMethod: str

@app.get("/")
def read_root():
    return {"message": "Hello, Next.js World!"}

@app.post("/send_carprice")
def carprice():
    return {"price": random.randint(1000, 50000)}

@app.post("/predict_churn")
def predict_churn(request: ChurnPredictionRequest):
    try:
        result = random.choice(["Churn", "Don't Churn"])
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
