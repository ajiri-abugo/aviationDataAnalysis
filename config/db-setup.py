import os
import psycopg2
import mysql.connector
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus

#load environment variables from .env file
load_dotenv()

# PostgreSQL
def create_postgres_db():
    try:
        conn = psycopg2.connect(
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PWD'),
            host=os.getenv('POSTGRES_HOST'),
            port=os.getenv('POSTGRES_PORT')
        )
    
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE travelagency;")
        print("PostgreSQL database 'travelagency' created successfully.")
    except Exception as e:
        print(f"Error creating PostgreSQL database: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# MySQL
def create_mysql_db():
    try:
        conn = mysql.connector.connect(
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PWD'),
            host=os.getenv('MYSQL_HOST')
        )
        
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS travelagency;")
        print("MySQL database 'travelagency' created or already exists.")
    except Exception as e:
        print(f"Error creating MySQL database: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# MongoDB
def create_mongo_db():
    try:
        username = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PWD')
        host = os.getenv('MONGO_HOST')
        port = os.getenv('MONGO_PORT')
        auth_db = os.getenv('MONGO_AUTH_DB')

        # Encode password to handle special characters
        encoded_password = quote_plus(password)

        #Mongo connection uri
        uri = f"mongodb://{username}:{encoded_password}@{host}:{port}/?authSource={auth_db}"
        #client = MongoClient("mongodb://localhost:27017/")
        client = MongoClient(uri)
        db = client["travelagency"]
        collection = db["test_collection"].insert_one({"init": "true"})  # Ensures DB creation
        print("MongoDB database 'travelagency' initialized successfully.")
    except Exception as e:
        print(f"Error initializing MongoDB database: {e}")
    finally:
        if client:
            client.close()

if __name__ == "__main__":
    create_postgres_db()
    create_mysql_db()
    create_mongo_db()
    print("Databases created successfully!")
