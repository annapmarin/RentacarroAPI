from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from fastapi import HTTPException
from models import Carro, Reserves, Usuaris
from schemas import ReservaCreate, ReservaUpdate, ReservaDelete

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

def modificar_reserva(db: Session, carro_id: int, data_inici: datetime, payload: ReservaUpdate):
    data_inici = data_inici.replace(tzinfo=None)

    # Comprovar que la reserva existeix
    reserva = (
        db.query(Reserves)
        .filter(
            Reserves.carro_id == carro_id,
            func.date(Reserves.data_inici) == data_inici.date()
        )
        .first()
    )

    if not reserva:
        raise HTTPException(status_code=404, detail="No s'ha trobat la reserva a modificar")

    # Calcular valors finals
    nou_carro_id = payload.carro_id if payload.carro_id is not None else reserva.carro_id
    nou_usuari_id = payload.usuari_id if payload.usuari_id is not None else reserva.usuari_id
    nova_data_inici = payload.data_inici.replace(tzinfo=None) if payload.data_inici is not None else reserva.data_inici
    nova_data_final = payload.data_final.replace(tzinfo=None) if payload.data_final is not None else reserva.data_final
    
    # Comprovar dates
    if nova_data_final <= nova_data_inici:
        raise HTTPException(status_code=400, detail="La data final ha de ser posterior a la data d'inici")
    
    # Comprovar que el nou carro existeix
    if payload.carro_id is not None:
        carro = db.query(Carro).filter(Carro.id == payload.carro_id).first()
        if not carro:
            raise HTTPException(status_code=404, detail="El carro no existeix")
        
    # Comprovar que el nou usuari existeix
    if payload.usuari_id is not None:
        usuari = db.query(Usuaris).filter(Usuaris.id == payload.usuari_id).first()
        if not usuari:
            raise HTTPException(status_code=404, detail="L'usuari no existeix")

    # Comprovar solapaments
    solapa = (
        db.query(Reserves)
        .filter(
            Reserves.carro_id == nou_carro_id,
            Reserves.data_inici < nova_data_final,
            Reserves.data_final > nova_data_inici,
            ~((Reserves.carro_id == reserva.carro_id) & (Reserves.data_inici == reserva.data_inici))
        )
        .first()
    )
    if solapa:
        raise HTTPException(status_code=409, detail="El carro no està disponible en aquest període")
    
    # Aplicar canvis
    reserva.carro_id = nou_carro_id
    reserva.usuari_id = nou_usuari_id
    reserva.data_inici = nova_data_inici
    reserva.data_final = nova_data_final
    
    db.commit()
    db.refresh(reserva)
    
    return {"msg": "Reserva modificada amb èxit"}

def eliminar_reserva(db: Session, carro_id: int, data_inici: datetime):
    data_inici = data_inici.replace(tzinfo=None)
    
    # Comprovar que la reserva existeix
    reserva = (
        db.query(Reserves)
        .filter(
            Reserves.carro_id == carro_id,
            Reserves.data_inici == data_inici
        )
        .first()
    )
    if not reserva:
        raise HTTPException(status_code=404, detail="No s'ha trobat la reserva a eliminar")
    
    db.delete(reserva)
    db.commit()