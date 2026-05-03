from fastapi import APIRouter, Query
from app.schemas.market_schema import MarketPriceCreate
from app.services.market_service import add_market_price, get_market_prices

router = APIRouter()

@router.post("/market-prices")
def create_market_price(data: MarketPriceCreate):
    return add_market_price(data)

@router.get("/market-prices")
def list_market_prices(crop: str = Query(None)):
    return get_market_prices(crop)