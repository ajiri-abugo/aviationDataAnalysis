from pymongo import MongoClient
from urllib.parse import quote_plus

# MongoDB connection details
host = "127.0.0.1"
port = 27017
username = "ajiri"
password = "ajiri23@24"
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