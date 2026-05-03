from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    crop_id: int
    actual_price: int
    sold_date: str