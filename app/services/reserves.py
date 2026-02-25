from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import HTTPException
from models import Carro, Reserves, Usuaris
from schemas import ReservaCreate

def get_reserves_per_periode(db: Session, data: str):
    try:
        inici = datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Data no vàlida, format ha de ser YYYY-MM-DD")

    final = inici + timedelta(days=7)

    reserves = (
        db.query(
            Carro.nom.label("nom_carro"),
            Reserves.data_inici,
            Reserves.data_final,
        )
        .join(Reserves, Reserves.carro_id == Carro.id)
        .filter(
            Reserves.data_inici < final,
            Reserves.data_final > inici
        )
        .all()
    )

    return [
        {"nom_carro": r.nom_carro, "data_inici": r.data_inici, "data_final": r.data_final}
        for r in reserves
    ]

def crear_nova_reserva(db: Session, payload: ReservaCreate):
    carro = db.query(Carro).filter(Carro.id == payload.carro_id).first()
    if not carro:
        raise HTTPException(status_code=404, detail="Carro no trobat")

    usuari = db.query(Usuaris).filter(Usuaris.id == payload.usuari_id).first()
    if not usuari:
        raise HTTPException(status_code=404, detail="Usuari no trobat")

    if payload.data_final <= payload.data_inici:
        raise HTTPException(status_code=400, detail="La data final ha de ser posterior a la data d'inici")

    solapa = (
        db.query(Reserves)
        .filter(
            Reserves.carro_id == payload.carro_id,
            Reserves.data_inici < payload.data_final,
            Reserves.data_final > payload.data_inici
        )
        .first()
    )

    if solapa:
        raise HTTPException(status_code=409, detail="El carro no està disponible en aquest període")

    nova_reserva = Reserves(
        carro_id=payload.carro_id,
        usuari_id=payload.usuari_id,
        data_inici=payload.data_inici.replace(tzinfo=None),
        data_final=payload.data_final.replace(tzinfo=None)
    )

    db.add(nova_reserva)
    db.commit()

    return {"msg": "Reserva creada amb èxit"}