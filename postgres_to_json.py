import psycopg2
import json
import os
from dotenv import load_dotenv

# ✅ Load .env
load_dotenv(dotenv_path=".env")

password = os.getenv("DB_PASSWORD")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="stockdb",
    user="postgres",
    password=password
)

cur = conn.cursor()

# Fetch data
cur.execute("SELECT * FROM google_stock")
rows = cur.fetchall()

# Column names
columns = [desc[0] for desc in cur.description]

# Convert to JSON
documents = []
for row in rows:
    documents.append(dict(zip(columns, row)))

cur.close()
conn.close()

print("Total records:", len(documents))
print(json.dumps(documents[0], indent=2, default=str))
