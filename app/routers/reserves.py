from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import ReservaPeriodeResponse, ReservaCreate
from app.services import reserves as reserves_service

router = APIRouter(prefix="/reserves", tags=["reserves"])

@router.get("/{data}", response_model=list[ReservaPeriodeResponse])
def get_reserves_periode(data: str, db: Session = Depends(get_db)):
    return reserves_service.get_reserves_per_periode(db, data)

@router.post("")
def crear_reserva(payload: ReservaCreate, db: Session = Depends(get_db)):
    return reserves_service.crear_nova_reserva(db, payload)