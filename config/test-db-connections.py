import os
import psycopg2
import mysql.connector
from pymongo import MongoClient

# Load environment variables
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "host.docker.internal")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB = os.getenv("POSTGRES_DB", "testdb")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")

MYSQL_HOST = os.getenv("MYSQL_HOST", "host.docker.internal")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_DB = os.getenv("MYSQL_DB", "testdb")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")

MONGO_HOST = os.getenv("MONGO_HOST", "host.docker.internal")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "testdb")


def test_postgres():
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        print("✅ PostgreSQL Connection Successful!")
        conn.close()
    except Exception as e:
        print(f"❌ PostgreSQL Connection Failed: {e}")


def test_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DB,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        print("✅ MySQL Connection Successful!")
        conn.close()
    except Exception as e:
        print(f"❌ MySQL Connection Failed: {e}")


def test_mongo():
    try:
        client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
        db = client[MONGO_DB]
        db.command("ping")  # Check if MongoDB is reachable
        print("✅ MongoDB Connection Successful!")
    except Exception as e:
        print(f"❌ MongoDB Connection Failed: {e}")


if __name__ == "__main__":
    print("🔍 Testing Database Connections...\n")
    test_postgres()
    test_mysql()
    test_mongo()
