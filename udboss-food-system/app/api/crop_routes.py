from fastapi import APIRouter
from app.schemas.crop_schema import CropCreate
from app.services.crop_service import create_crop, get_crops

router = APIRouter()

@router.post("/crops")
def add_crop(crop: CropCreate):
    return create_crop(crop)

@router.get("/crops")
def list_crops():
    return get_crops()