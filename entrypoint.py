from app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("entrypoint:app", host="localhost", reload=True)