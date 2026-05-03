from fastapi import APIRouter
from app.services.recommendation_service import generate_recommendation

router = APIRouter()

@router.get("/recommend/{crop_id}")
def recommend(crop_id: int):
    return generate_recommendation(crop_id)