from fastapi import FastAPI
from src.api import auth

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI rodando com MySQL!"}


app.include_router(auth.router)