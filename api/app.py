from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")

app = FastAPI()

# ---------------- DB CONNECTIONS ---------------- #

def get_pg_connection():
    return psycopg2.connect(
        host="localhost",
        database="stockdb",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )

mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["stockdb"]
mongo_collection = mongo_db["google_stock"]

# ---------------- MODEL ---------------- #

class Stock(BaseModel):
    trade_date: str
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    adj_close_price: float
    volume: int

# ---------------- ROUTES ---------------- #

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

# Get PostgreSQL data
@app.get("/stocks")
def get_stocks():
    conn = get_pg_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM google_stock LIMIT 10")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return [dict(zip(columns, row)) for row in rows]

# Get MongoDB data
@app.get("/mongo-stocks")
def get_mongo_stocks():
    data = list(mongo_collection.find({}, {"_id": 0}))
    return data[:10]

# Insert data
@app.post("/stocks")
def add_stock(stock: Stock):
    conn = get_pg_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO google_stock 
            (trade_date, open_price, high_price, low_price, close_price, adj_close_price, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            stock.trade_date,
            stock.open_price,
            stock.high_price,
            stock.low_price,
            stock.close_price,
            stock.adj_close_price,
            stock.volume
        ))

        conn.commit()

        mongo_collection.insert_one(stock.dict())

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()

    return {"message": "Inserted into PostgreSQL + MongoDB ✅"}

# Search by date
@app.get("/stocks/{trade_date}")
def get_stock_by_date(trade_date: str):
    conn = get_pg_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM google_stock WHERE trade_date = %s",
        (trade_date,)
    )

    row = cur.fetchone()
    columns = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Stock not found")

    return dict(zip(columns, row))