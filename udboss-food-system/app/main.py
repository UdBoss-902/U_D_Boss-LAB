from fastapi import FastAPI
from app.db.database import create_tables
from app.api.farmer_routes import router as farmer_router
from app.api.crop_routes import router as crop_router



app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

app.include_router(farmer_router)
app.include_router(crop_router)

@app.get("/")
def root():
    return {"message": "UDBOSS Food System Running"}