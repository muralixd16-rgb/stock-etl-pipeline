# 📊 ETL Stock Data Pipeline (CSV → PostgreSQL → MongoDB)

## 🚀 Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** that processes stock market data across multiple data storage systems.

The pipeline extracts stock data from a CSV file, loads it into a PostgreSQL database, transforms it into JSON format, and finally stores it in a MongoDB NoSQL database.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, Psycopg2, PyMongo, Python-Dotenv
* **Databases:** PostgreSQL (Relational), MongoDB (NoSQL)

---

## 🔄 Workflow Architecture

```
CSV File → PostgreSQL → JSON Transformation → MongoDB
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
├── main.py                     # Entry point to run pipeline
│
├── google.csv                  # Input dataset
├── requirements.txt            # Dependencies
├── .gitignore                  # Ignored files
├── .env (ignored)              # Environment variables (not pushed)
│
├── README.md                   # Project documentation
│
├── old_scripts/ (optional)     # Legacy scripts (local only, ignored)
│   ├── load_csv_to_postgres.py
│   ├── postgres_to_json.py
│   └── postgres_to_mongo.py
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
* Create a table:

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

### 5️⃣ Run the Pipeline

#### Step 1: Load CSV into PostgreSQL

```
python load_csv_to_postgres.py
```

#### Step 2: Convert PostgreSQL data to JSON

```
python postgres_to_json.py
```

#### Step 3: Load data into MongoDB

```
python postgres_to_mongo.py
```

---

## 📊 Features

* ✔️ End-to-end ETL pipeline implementation
* ✔️ Integration of SQL and NoSQL databases
* ✔️ Secure credential handling using environment variables
* ✔️ Data transformation from structured to semi-structured format
* ✔️ Scalable and modular design

---
## 📚 Key Learnings

- Built an end-to-end ETL pipeline from scratch  
- Learned integration between relational (PostgreSQL) and NoSQL (MongoDB) databases  
- Gained hands-on experience with data transformation and JSON conversion  
- Implemented secure credential management using environment variables (.env)  
- Understood real-world data engineering workflows  

## 🔒 Security Best Practices

* Sensitive credentials are stored in `.env`
* `.env` is excluded using `.gitignore`
* No hardcoded passwords in source code

---

## 🎯 Use Cases

* Data engineering pipelines
* Data migration between databases
* Real-world ETL workflows
* Learning SQL + NoSQL integration

---

## 💡 Future Enhancements

* Add data validation and cleaning
* Automate pipeline using Airflow
* Add API layer using FastAPI
* Deploy pipeline using Docker

---

## 👨‍💻 Author

**Murali Manohar**

