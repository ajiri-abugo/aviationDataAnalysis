import os
import psycopg2
import mysql.connector
from pymongo import MongoClient

# Load environment variables
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB = os.getenv("POSTGRES_DB", "testdb")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PWD = os.getenv("POSTGRES_PWD")

MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_DB = os.getenv("MYSQL_DB", "testdb")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PWD = os.getenv("MYSQL_PWD")

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "testdb")
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PWD = os.getenv("MYSQL_PWD")
MONGO_AUTHENTICATION_DB = os.getenv("MONGO_AUTHENTICATION_DB", "admin")


def test_postgres():
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PWD
        )
        print("PostgreSQL Connection Successful!")
        conn.close()
    except Exception as e:
        print(f"PostgreSQL Connection Failed: {e}")


def test_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DB,
            user=MYSQL_USER,
            password=MYSQL_PWD
        )
        print("MySQL Connection Successful!")
        conn.close()
    except Exception as e:
        print(f"MySQL Connection Failed: {e}")


def test_mongo():
    try:
        # Encode password to handle special characters
        encoded_password = quote_plus(MONGO_PWD)

        # Construct MongoDB connection URI
        uri = f"mongodb://{MONGO_USER}:{encoded_password}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource={MONGO_AUTH_DB}"
        client = MongoClient(uri)
        db = client[MONGO_DB]
        db.command("ping")  # Check if MongoDB is reachable
        #db.runCommand({ping: 1})
        print("MongoDB Connection Successful!")
        client.close()
    except Exception as e:
        print(f"MongoDB Connection Failed: {e}")


if __name__ == "__main__":
    print("Testing Database Connections...\n")
    test_postgres()
    test_mysql()
    test_mongo()