import os
from dotenv import load_dotenv
import mysql.connector

#load environment variables from .env file
load_dotenv()

#connection details
username = os.getenv('MYSQL_USER')
dbname = os.getenv('MYSQL_DB')
pwd = os.getenv('MYSQL_PWD')
d_host = os.getenv('MYSQL_HOST')
d_port = os.getenv('MYSQL_PORT')

# function to connect to database
def get_mysql_db():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="d_host",
            user="username",
            password="pwd",
            port="d_port",
            database="dbname")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("error connecting to mysql database")

if __name__ == "__main__":
    get_mysql_db()
