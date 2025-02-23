import os
import psycopg2
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

#postgres connection details
dbname = os.getenv('POSTGRES_DB')
username = os.getenv('POSTGRES_USER'),
d_pwd = os.getenv('POSTGRES_PWD'),
d_host = os.getenv('POSTGRES_HOST'),
d_port = os.getenv('POSTGRES_PORT')

def get_postgres_db():
    try:
        conn = psycopg2.connect(
            database="dbname",
            user="username",
            password="d_pwd",
            host="d_host",
            port="d_port"
        )
        return conn
        print("Connected to Postgres Data Warehouse")
    except (psycopg2.DatabaseError, Exception) as err:
        print(f"Error: {err}")
        print("Failed to connect to postgres")

if __name__ == "__main__":
    get_postgres_db()