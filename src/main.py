from fastapi import FastAPI
from src.api import auth
from src.api.v1 import product

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI rodando com MySQL!"}


app.include_router(auth.router)
app.include_router(product.router)