from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import CarroResponse, DisponibilitatRequest
from app.services import carros as carros_service

router = APIRouter(prefix="/carros", tags=["carros"])

@router.get("", response_model=list[CarroResponse])
def get_carros(db: Session = Depends(get_db)):
    return carros_service.get_all_carros(db)

@router.post("/disponibilitat", response_model=dict[str, float])
def disponibilitat(payload: DisponibilitatRequest, db: Session = Depends(get_db)):
    if payload.data_final <= payload.data_inici:
        raise HTTPException(status_code=400, detail="La data final ha de ser posterior a la data d'inici")
    return carros_service.get_carros_disponibles(db, payload)