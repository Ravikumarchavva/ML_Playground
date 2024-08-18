from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variable
BASE_URL = os.getenv("BASE_URL")
NEXTJS_URL = os.getenv("NEXTJS_URL")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[BASE_URL,NEXTJS_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello next World"}

items = {
    1: {"name": "Foo", "price": 42.00},
    2: {"name": "Bar", "price": 24.00, "is_offer": True},
    3: {"name": "Baz", "price": 19.50},
}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "details": items.get(item_id, {})}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

import apis.carprice as cp
@app.get('/carprice')
def get_car_price():
    return {"price": cp.carprice()}

import apis.churn as ch

@app.get('/churn')
def get_churn_prediction():
    return {"churn":ch.churn}

import apis.imageClassification as c

@app.post('/imageclassification')
def classify_image():
    return {"image":c.imageClassification()}