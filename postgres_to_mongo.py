import psycopg2
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ✅ Load .env
load_dotenv(dotenv_path=".env")

password = os.getenv("DB_PASSWORD")

# PostgreSQL connection
pg_conn = psycopg2.connect(
    host="localhost",
    database="stockdb",
    user="postgres",
    password=password
)

pg_cur = pg_conn.cursor()
pg_cur.execute("SELECT * FROM google_stock")

rows = pg_cur.fetchall()
columns = [desc[0] for desc in pg_cur.description]

# Convert to documents
documents = []
for row in rows:
    record = dict(zip(columns, row))
    record["trade_date"] = str(record["trade_date"])
    documents.append(record)

pg_cur.close()
pg_conn.close()

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["stockdb"]
mongo_collection = mongo_db["google_stock"]

mongo_collection.insert_many(documents)

print("✅ Data inserted into MongoDB")