from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime
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
    img = Column(String(50))
    
    reserves = relationship("Reserves", back_populates="carro")

class Usuaris(Base):
    __tablename__ = "usuaris"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(15), unique=True)
    nom_complet = Column(String(100))
    contrasenya = Column(String(255))
    alta = Column(DateTime)
    email = Column(String(100), unique=True)
    telefon = Column(String(20))
    
    reserves = relationship("Reserves", back_populates="usuari")


class Reserves(Base):
    __tablename__ = "reserves"

    carro_id = Column(Integer, ForeignKey("carros.id"), primary_key=True, nullable=False)
    data_inici = Column(DateTime, primary_key=True, nullable=False)
    data_final = Column(DateTime, nullable=False)
    usuari_id = Column(Integer, ForeignKey("usuaris.id"), nullable=False)

    carro = relationship("Carro", back_populates="reserves")
    usuari = relationship("Usuaris", back_populates="reserves")