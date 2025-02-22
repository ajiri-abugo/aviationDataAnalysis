import psycopg2
import mysql.connector
import pymongo

# PostgreSQL
def create_postgres_db():
    conn = psycopg2.connect(
        dbname="postgres", user="airflow", password="yourpassword", host="localhost"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE airflow;")
    cursor.close()
    conn.close()

# MySQL
def create_mysql_db():
    conn = mysql.connector.connect(user="root", password="yourpassword", host="localhost")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS airflow;")
    cursor.close()
    conn.close()

# MongoDB (creates DB automatically when a collection is inserted)
def create_mongo_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client["aviation_data"]["test_collection"].insert_one({"init": "true"})  # Ensures DB creation

if __name__ == "__main__":
    create_postgres_db()
    create_mysql_db()
    create_mongo_db()
    print("✅ Databases created successfully!")
