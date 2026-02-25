from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
from schemas import ReservaPeriodeResponse, ReservaCreate, ReservaUpdate
from app.services import reserves as reserves_service
from datetime import datetime

router = APIRouter(prefix="/reserves", tags=["reserves"])

@router.get("/{data}", response_model=list[ReservaPeriodeResponse],
            summary="Obtenir reserves segons període",
            description="Retorna totes les reserves actives en un període determinat a partir d'una data.")
def get_reserves_periode(data: str, db: Session = Depends(get_db)):
    return reserves_service.get_reserves_per_periode(db, data)

@router.post("",
            summary="Crear una nova reserva",
            description="Crea una nova reserva assignant un carro a un usuari per un període de temps.")
def crear_reserva(payload: ReservaCreate, db: Session = Depends(get_db)):
    return reserves_service.crear_nova_reserva(db, payload)

@router.put("/{carro_id}/{data_inici}",
            summary="Modificar una reserva existent",
            description="Modifica els detalls d'una reserva existent identificada pel carro i la data d'inici.")
def put_reserva(carro_id: int, data_inici: str, payload: ReservaUpdate, db: Session = Depends(get_db)):
    data_inici = datetime.fromisoformat(data_inici)
    return reserves_service.modificar_reserva(db, carro_id, data_inici, payload)

@router.delete("/{carro_id}/{data_inici}", status_code=204,
            summary="Eliminar una reserva",
            description="Elimina una reserva existent identificada pel carro i la data d'inici.")
def delete_reserva(carro_id: int, data_inici: str, db: Session = Depends(get_db)):
    data_inici = datetime.fromisoformat(data_inici)
    reserves_service.eliminar_reserva(db, carro_id, data_inici)
    return Response(status_code=204)