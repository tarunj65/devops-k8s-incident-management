from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.schemas.incident import (IncidentCreate, IncidentUpdate, IncidentResponse)

router = APIRouter(prefix="/incidents", tags=["Incidents"])

@router.post("/", response_model=IncidentResponse, status_code=status.HTTP_201_CREATED)
def create_incident(incident: IncidentCreate, db: Session = Depends(get_db)):
    new_incident = Incident(**incident.model_dump())

    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)

    return new_incident


@router.get("/", response_model=list[IncidentResponse])
def get_incidents(db: Session = Depends(get_db)):
    return db.scalars(select(Incident).order_by(Incident.id)).all()


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.get(Incident, incident_id)
    
    if incident is None:
        raise HTTPException(status_code=404,
                            detail="Incident not found")
    return incident


@router.put("/{incident_id}", response_model=IncidentResponse)
def update_incident(incident_id: int, update_data: IncidentUpdate, db: Session = Depends(get_db)):
    incident = db.get(Incident, incident_id)

    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    changes = update_data.model_dump(exclude_unset=True)

    if any(value is None for value in changes.values()):
        raise HTTPException(status_code=422, detail="Incident fields cannot be null")

    for field, value in changes.items():
        setattr(incident, field, value)

    db.commit()
    db.refresh(incident)

    return incident


@router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.get(Incident, incident_id)

    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    db.delete(incident)
    db.commit()
