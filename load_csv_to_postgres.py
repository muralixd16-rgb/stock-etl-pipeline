import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# ✅ Force load .env file (IMPORTANT FIX)
load_dotenv(dotenv_path=".env")

# Debug check (remove later)
password = os.getenv("DB_PASSWORD")
print("DEBUG PASSWORD:", password)

# 1. Read CSV
df = pd.read_csv("google.csv")

# 2. Rename columns
df.columns = [
    "trade_date",
    "open_price",
    "high_price",
    "low_price",
    "close_price",
    "adj_close_price",
    "volume"
]

# 3. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="stockdb",
    user="postgres",
    password=password
)

cur = conn.cursor()

# 4. Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO google_stock
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# 5. Commit and close
conn.commit()
cur.close()
conn.close()

print("✅ CSV data successfully loaded into PostgreSQL")