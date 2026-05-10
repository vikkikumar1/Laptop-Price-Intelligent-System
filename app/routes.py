from fastapi import APIRouter
from app.schemas import LaptopData
from model.predict import predict_price

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Laptop Price PredictionAPI is Running"}

@router.post("/predict")
def predict(data: LaptopData):

    input_dict = {
        'Company': data.company,
        'TypeName': data.type,
        'Ram': data.ram,
        'Weight': data.weight,
        'Touchscreen': data.touchscreen,
        'Ips': data.ips,
        'ppi': data.ppi,
        'Cpu brand': data.cpu,
        'HDD': data.hdd,
        'SSD': data.ssd,
        'Gpu brand': data.gpu,
        'os': data.os
    }

    price = predict_price(input_dict)

    return {"predicted_price": price}