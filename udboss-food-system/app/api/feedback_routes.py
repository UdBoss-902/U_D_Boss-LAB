from fastapi import APIRouter
from app.schemas.feedback_schema import FeedbackCreate
from app.services.feedback_service import add_feedback

router = APIRouter()

@router.post("/feedback")
def create_feedback(data: FeedbackCreate):
    return add_feedback(data)