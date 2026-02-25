from datetime import date, datetime
from pydantic import BaseModel, ConfigDict
from typing import Literal, Optional


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

class ReservaUpdate(BaseModel):
    carro_id: Optional[int] = None
    usuari_id: Optional[int] = None
    data_inici: Optional[datetime] = None
    data_final: Optional[datetime] = None

class ReservaPeriodeResponse(BaseModel):
    nom_carro: str
    data_inici: datetime
    data_final: datetime
    

class DisponibilitatRequest(BaseModel):
    data_inici: date
    data_final: date