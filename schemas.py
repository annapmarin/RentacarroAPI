from pydantic import BaseModel
from typing import Literal

class CarroCreate(BaseModel):
    nom: str
    classe: Literal["basic", "1cavall", "2cavalls"]
    preu: float
    descripcio: str
    img: str

class CarroUpdate(BaseModel):
    nom: str
    classe: Literal["basic", "1cavall", "2cavalls"]
    preu: float
    descripcio: str
    img: str

class CarroResponse(BaseModel):
    id: int
    nom: str
    classe: Literal["basic", "1cavall", "2cavalls"]
    preu: float
    descripcio: str
    img: str

    class Config:
        orm_mode = True