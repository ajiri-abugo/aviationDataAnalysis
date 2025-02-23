import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from urllib.parse import quote_plus

#load environment variables from .env file
load_dotenv()

# MongoDB connection details
host = os.getenv('MONGO_HOST')
port = os.getenv('MONGO_PORT')
username = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PWD')
database = os.getenv('MONGO_DB')
auth_db = os.getenv('MONGO_AUTH_DB')

# Encode password to handle special characters
encoded_password = quote_plus(password)

# Construct MongoDB connection URI
uri = f"mongodb://{username}:{encoded_password}@{host}:{port}/{database}?authSource={auth_db}"

# Create a function to return the database connection
def get_mongo_db():
    try:
        client = MongoClient(uri)
        db = client[database]
        return db, client  # Returns the database object and client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error: {e}")
        print("could not connect to mongo database")

if __name__ == "__main__":
    get_mongo_db()