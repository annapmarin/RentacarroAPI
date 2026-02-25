from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import ReservaPeriodeResponse, ReservaCreate, ReservaUpdate
from app.services import reserves as reserves_service
from datetime import datetime

router = APIRouter(prefix="/reserves", tags=["reserves"])

@router.get("/{data}", response_model=list[ReservaPeriodeResponse])
def get_reserves_periode(data: str, db: Session = Depends(get_db)):
    return reserves_service.get_reserves_per_periode(db, data)

@router.post("")
def crear_reserva(payload: ReservaCreate, db: Session = Depends(get_db)):
    return reserves_service.crear_nova_reserva(db, payload)

@router.put("/{carro_id}/{data_inici}")
def put_reserva(carro_id: int, data_inici: datetime, payload: ReservaUpdate, db: Session = Depends(get_db)):
    return reserves_service.modificar_reserva(db, carro_id, data_inici, payload)