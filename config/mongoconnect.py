import os
from dotenv import load_dotenv
from pymongo import MongoClient
from urllib.parse import quote_plus

#load environment variables from .env file
load_dotenv()

# MongoDB connection details
host = "127.0.0.1"
port = 27017
username = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PWD')
database = "travelagency"

# Encode password to handle special characters
encoded_password = quote_plus(password)

# Construct MongoDB connection URI
uri = f"mongodb://{username}:{encoded_password}@{host}:{port}/{database}?authSource=admin"
#connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(username,password,host)

# Create a function to return the database connection
def get_mongo_db():
    client = MongoClient(uri)
    db = client[database]
    return db, client  # Returns the database object and client