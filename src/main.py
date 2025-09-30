import os
import mysql.connector
from fastapi import FastAPI

app = FastAPI()

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "0.0.0.0"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "root"),
    "database": os.getenv("MYSQL_DATABASE", "meubanco"),
    "port": int(os.getenv("MYSQL_PORT", 3308)),
}

@app.get("/")
def read_root():
    return {"message": "FastAPI rodando com MySQL!"}

@app.get("/db")
def test_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    conn.close()
    return {"db_time": result[0]}
