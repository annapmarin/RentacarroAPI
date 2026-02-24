from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from database import Base

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=True)
    classe = Column(
        Enum("basic", "1cavall", "2cavalls", name="classe_enum")
    )
    preu = Column(Float)
    descripcio = Column(String(250))
    img = Column(String(250))

