from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Carro
from schemas import CarroResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "API Funcionant!"}

@app.get("/carros", response_model=list[CarroResponse])
def get_carros(db: Session = Depends(get_db)):
    carros = db.query(Carro).all()
    return carros

if __name__ == "__main__":
    uvicorn.run("entrypoint:app", host="localhost", reload=True)