from sqlalchemy.orm import Session
from sqlalchemy import not_
from models import Carro, Reserves
from schemas import DisponibilitatRequest

def get_all_carros(db: Session):
    return db.query(Carro).all()

def get_carros_disponibles(db: Session, payload: DisponibilitatRequest) -> dict[str, float]:
    reservats = (
        db.query(Reserves.carro_id)
        .filter(
            Reserves.data_inici < payload.data_final,
            Reserves.data_final > payload.data_inici
        )
    )

    carros_disponibles = (
        db.query(Carro)
        .filter(not_(Carro.id.in_(reservats)))
        .all()
    )

    dies = (payload.data_final - payload.data_inici).days
    return {carro.nom: carro.preu * dies for carro in carros_disponibles}