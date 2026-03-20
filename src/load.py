import psycopg2
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(dotenv_path=".env")

def load_to_postgres(df):
    conn = psycopg2.connect(
        host="localhost",
        database="stockdb",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO google_stock
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Loaded into PostgreSQL")


def load_to_mongo(df):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["stockdb"]
    collection = db["google_stock"]

    data = df.to_dict(orient="records")

    for record in data:
        record["trade_date"] = str(record["trade_date"])

    collection.insert_many(data)

    print("✅ Loaded into MongoDB")