from pydantic import BaseModel

class MarketPriceCreate(BaseModel):
    market: str
    crop: str
    date: str
    price: int

class MarketPriceResponse(BaseModel):
    id: int
    market: str
    crop: str
    date: str
    price: int