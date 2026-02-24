from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "API Funcionant!"}

if __name__ == "__main__":
    uvicorn.run("entrypoint:app", host="localhost", reload=True)