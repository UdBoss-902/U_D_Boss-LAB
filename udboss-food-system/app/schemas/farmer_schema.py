from pydantic import BaseModel

class FarmerCreate(BaseModel):
    name: str
    location: str
    phone: str

class FarmerResponse(BaseModel):
    id: int
    name: str
    location: str
    phone: str