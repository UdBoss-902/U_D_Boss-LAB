from fastapi import APIRouter
from app.schemas.farmer_schema import FarmerCreate
from app.services.farmer_service import create_farmer, get_farmers

router = APIRouter()

@router.post("/farmers")
def add_farmer(farmer: FarmerCreate):
    return create_farmer(farmer)

@router.get("/farmers")
def list_farmers():
    return get_farmers()