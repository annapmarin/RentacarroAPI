from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import CarroResponse, DisponibilitatRequest
from app.services import carros as carros_service

router = APIRouter(prefix="/carros", tags=["carros"])

@router.get("", response_model=list[CarroResponse],
            summary="Obtenir tots els carros",
            description="Retorna el llistat complet de carros amb els seus detalls.")
def get_carros(db: Session = Depends(get_db)):
    return carros_service.get_all_carros(db)

@router.post("/disponibilitat", response_model=dict[str, float], tags=["disponibilitat"],
            summary="Consultar disponibilitat de carros",
            description="Retorna els carros disponibles i el seu preu total per un període especificat.")
def disponibilitat(payload: DisponibilitatRequest, db: Session = Depends(get_db)):
    if payload.data_final <= payload.data_inici:
        raise HTTPException(status_code=400, detail="La data final ha de ser posterior a la data d'inici")
    return carros_service.get_carros_disponibles(db, payload)