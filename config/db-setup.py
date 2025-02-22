import os
import psycopg2
import mysql.connector
from pymongo import MongoClient
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

# PostgreSQL
def create_postgres_db():
    conn = psycopg2.connect(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PWD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT')
    )
    
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE travelagency;")
    cursor.close()
    conn.close()

# MySQL
def create_mysql_db():
    conn = mysql.connector.connect(
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PWD'),
        host=os.getenv('MYSQL_HOST')
    )
        
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS travelagency;")
    cursor.close()
    conn.close()

# MongoDB
def create_mongo_db():
    uri = f"mongodb://{username}:{encoded_password}@{host}:{port}?authSource={auth_db}"
    #client = MongoClient("mongodb://localhost:27017/")
    client = MongoClient(uri)
    db = client["travelagency"]
    collection = db["test_collection"].insert_one({"init": "true"})  # Ensures DB creation

if __name__ == "__main__":
    create_postgres_db()
    create_mysql_db()
    create_mongo_db()
    print("Databases created successfully!")
