# 📊 ETL Stock Data Pipeline + FastAPI (CSV → PostgreSQL → MongoDB)

## 🚀 Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** integrated with a **FastAPI backend** to serve stock market data through REST APIs.

The pipeline extracts stock data from a CSV file, loads it into a PostgreSQL database, transforms it into JSON format, and stores it in a MongoDB NoSQL database.
Additionally, FastAPI is used to expose this data via APIs for easy access and integration.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, Psycopg2, PyMongo, Python-Dotenv, FastAPI, Pydantic
* **Databases:** PostgreSQL (Relational), MongoDB (NoSQL)
* **API Server:** Uvicorn

---

## 🔄 Workflow Architecture

```
CSV File → PostgreSQL → JSON Transformation → MongoDB → FastAPI API
```

---

## 📂 Project Structure

```
stock_project/
│
├── src/                        # Modular ETL components
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py                     # FastAPI application (API layer)
│
├── google.csv                  # Input dataset
├── requirements.txt            # Dependencies
├── .gitignore                  # Ignored files
├── .env (ignored)              # Environment variables (not pushed)
│
├── README.md                   # Project documentation
│
├── old_scripts/ (optional)     # Legacy scripts (local only, ignored)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/stock-etl-pipeline.git
cd stock-etl-pipeline
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
DB_PASSWORD=your_postgresql_password
```

---

### 4️⃣ Setup PostgreSQL Database

* Create a database named: `stockdb`

```sql
CREATE TABLE google_stock (
    trade_date DATE,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    adj_close_price FLOAT,
    volume BIGINT
);
```

---

### 5️⃣ Run the ETL Pipeline

```
python main.py
```

---

## 🌐 FastAPI API Layer

This project includes a FastAPI backend to expose stock data through REST APIs.

### ▶️ Run the API

```
uvicorn main:app --reload
```

---

### 📌 Available Endpoints

```
GET /          → Check API status  
GET /stocks    → Fetch all stock data from PostgreSQL  
```

---

### 📍 Swagger UI (Interactive Docs)

```
http://127.0.0.1:8000/docs
```

---

## 📊 Features

* ✔️ End-to-end ETL pipeline implementation
* ✔️ Integration of SQL and NoSQL databases
* ✔️ REST API built using FastAPI
* ✔️ Structured API responses using Pydantic
* ✔️ Secure credential handling using environment variables
* ✔️ Scalable and modular design

---

## 📚 Key Learnings

* Built an end-to-end ETL pipeline from scratch
* Integrated PostgreSQL (SQL) and MongoDB (NoSQL)
* Developed REST APIs using FastAPI
* Used Pydantic for data validation and serialization
* Understood real-world data engineering + backend workflows

---

## 🔒 Security Best Practices

* Sensitive credentials are stored in `.env`
* `.env` is excluded using `.gitignore`
* No hardcoded passwords in source code

---

## 🎯 Use Cases

* Data engineering pipelines
* Backend API development
* Data migration between databases
* Real-world ETL workflows

---

## 💡 Future Enhancements

* Add filtering/search API endpoints
* Automate pipeline using Airflow
* Deploy API using Docker / Cloud
* Add authentication to API

---

## 👨‍💻 Author

**Murali Manohar**

