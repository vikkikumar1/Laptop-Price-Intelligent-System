from pydantic import BaseModel

class LaptopData(BaseModel):
    company: str
    type: str
    ram: int
    weight: float
    touchscreen: int
    ips: int
    ppi: float
    cpu: str
    hdd: int
    ssd: int
    gpu: str
    os: str