from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("entrypoint:app", 
                host="localhost",
                reload=True)