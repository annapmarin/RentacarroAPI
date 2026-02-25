from datetime import date, datetime
from pydantic import BaseModel, ConfigDict
from typing import Literal


class CarroResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nom: str
    classe: Literal["basic", "1cavall", "2cavalls"]
    preu: float
    descripcio: str
    img: str
    
class ReservaCreate(BaseModel):
    carro_id: int
    usuari_id: int
    data_inici: datetime
    data_final: datetime

class ReservaPeriodeResponse(BaseModel):
    nom_carro: str
    data_inici: datetime
    data_final: datetime
    

class DisponibilitatRequest(BaseModel):
    data_inici: date
    data_final: date