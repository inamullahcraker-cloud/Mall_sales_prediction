"""
FastAPI application for Store Item Sales Forecasting.
"""

from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.config import load_config
from src.logger import get_logger
from src.predict import Predictor

logger = get_logger(__name__)

config = load_config()

app = FastAPI(

    title="Store Item Sales Forecasting API",

    version="1.0.0",

    description="Predict future sales using the trained ML pipeline.",

)

from fastapi.middleware.cors import CORSMiddleware
from src.api.analytics import router as analytics_router

predictor = Predictor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytics_router)
# =====================================================
# Request Schema
# =====================================================

class PredictionRequest(BaseModel):

    date: date

    store: int

    item: int


# =====================================================
# Response Schema
# =====================================================

class PredictionResponse(BaseModel):

    predicted_sales: float


# =====================================================
# Home
# =====================================================

@app.get("/")

def home():

    return {

        "message": "Store Item Sales Forecasting API",

        "version": "1.0.0",

    }


# =====================================================
# Health
# =====================================================

@app.get("/health")

def health():

    return {

        "status": "healthy"

    }


# =====================================================
# Prediction
# =====================================================

@app.post(
    "/predict",
    response_model=PredictionResponse,
)

def predict(request: PredictionRequest):

    try:

        prediction = predictor.predict(

            date=request.date,

            store=request.store,

            item=request.item,

        )

        return PredictionResponse(

            predicted_sales=float(prediction)

        )

    except Exception as error:

        logger.exception(error)

        raise HTTPException(

            status_code=500,

            detail=str(error),

        )
