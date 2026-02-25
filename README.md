# RentacarroAPI

API REST per gestionar el lloguer de carros. Permet administrar vehicles, reserves i consultar disponibilitat.

## Tecnologies
- Python 3.11+
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn

## Endpoints

### Carros
- GET    /carros                        Llista tots els carros
- POST   /carros/disponibilitat         Consulta carros disponibles per període

### Reserves
- GET    /reserves/{data}               Llista reserves d'un període
- POST   /reserves                      Crea una nova reserva
- PUT    /reserves/{carro_id}/{data}    Modifica una reserva
- DELETE /reserves/{carro_id}/{data}    Elimina una reserva

## Estructura del projecte

rentacarro-api/
├── app/
│   ├── routers/
│   │   ├── carros.py
│   │   └── reserves.py
│   └── services/
│       ├── carros.py
│       └── reserves.py
├── models.py
├── schemas.py
├── database.py
├── main.py
├── requirements.txt
└── .env