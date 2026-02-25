from fastapi import FastAPI
from app.routers import carros, reserves

app = FastAPI()

app.include_router(carros.router)
app.include_router(reserves.router)

@app.get("/")
def read_root():
    return {"msg": "API Funcionant!"}