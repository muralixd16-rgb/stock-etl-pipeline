# 📊 ETL Stock Data Pipeline + FastAPI

### *(CSV → PostgreSQL → MongoDB)*

---

## 🚀 Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** integrated with a **FastAPI backend**.

The pipeline extracts stock market data from a CSV file, transforms it, stores it in PostgreSQL, and then loads it into MongoDB.
The processed data is exposed through REST APIs using FastAPI.

---

## 🧠 Architecture

```
CSV → Extract → Transform → PostgreSQL → MongoDB → FastAPI
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **ETL:** Pandas
* **Databases:** PostgreSQL, MongoDB
* **Backend:** FastAPI
* **Libraries:** Psycopg2, PyMongo, Python-Dotenv
* **Server:** Uvicorn

---

## 📂 Project Structure

```
stock-etl-pipeline/
│
├── api/
│   └── main.py
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── run_pipeline.py
├── google.csv
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ▶️ How to Run

### 🔹 Run ETL Pipeline

```
python run_pipeline.py
```

### 🔹 Run FastAPI Server

```
uvicorn api.main:app --reload
```

### 🔹 Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

* `GET /` → API status
* `GET /stocks` → Fetch PostgreSQL data
* `GET /mongo-stocks` → Fetch MongoDB data
* `POST /stocks` → Insert new stock
* `GET /stocks/{trade_date}` → Get stock by date

---

## 📊 Features

* End-to-end ETL pipeline
* SQL + NoSQL integration
* REST API with FastAPI
* Modular code structure
* Secure environment variables



