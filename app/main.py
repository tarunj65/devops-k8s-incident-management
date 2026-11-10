from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.incidents import router as incident_router
from app.core.database import get_db

app = FastAPI(title="Incident Management API",
              version="1.0.0",
              description="Incident Management REST API for DevOps Kubernetes Project"
              )

app.include_router(incident_router)


@app.get("/")
def root():
    return {
            "application":"Incident Management API",
            "status":"running"
            }


@app.get("/health/live")
def liveness():
    return {"status":"alive"}


@app.get("/health/ready")
def readiness(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status":"ready"}

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )
