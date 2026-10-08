from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI(
    title="BuyWise API",
    description="Backend API for the BuyWise comparison platform.",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "buywise-api",
        "version": "0.1.0",
    }


@app.get("/api/health/database")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "connected",
        }

    except Exception as error:
        return {
            "status": "error",
            "database": "disconnected",
            "detail": str(error),
        }