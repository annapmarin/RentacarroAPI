from fastapi import FastAPI
from app.routers import carros, reserves

app = FastAPI(
    title="RentacarroAPI",
    version="0.1.0",
    description="API per gestionar la reserva de carros. Permet administrar carros, reserves i consultar disponibilitat.",
    openapi_tags=[
        {"name": "carros", "description": "Visualització i consulta de carros disponibles."},
        {"name": "reserves", "description": "Gestió de reserves: crear, modificar, eliminar i consultar períodes."},
        {"name": "disponibilitat", "description": "Consulta de disponibilitat dels carros."}
    ]
)

app.include_router(carros.router)
app.include_router(reserves.router)

@app.get("/")
def read_root():
    return {"msg": "API Funcionant!"}