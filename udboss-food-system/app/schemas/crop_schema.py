from pydantic import BaseModel

class CropCreate(BaseModel):
    farmer_id: int
    crop: str
    expected_harvest_date: str
    quantity: int

class CropResponse(BaseModel):
    id: int
    farmer_id: int
    crop: str
    expected_harvest_date: str
    quantity: int
    status: str