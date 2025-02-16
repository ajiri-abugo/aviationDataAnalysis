import sys
import os
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../../"))
from config.mongoconnect import get_mongo_db  # Import the connection function

# Get MongoDB database
db, client = get_mongo_db()

# Select collection
#collection = db["test_airport"]
collection = db["airports"]

# Path to the JSON file
#json_file_path = "/home/ajiri/project/aviationDataAnalysis/data/raw/test_airports.json"
json_file_path = "/home/ajiri/project/aviationDataAnalysis/data/raw/airports.json"

# Load and transform the JSON data
with open(json_file_path, "r") as file:
    data = json.load(file)  # Load JSON as dictionary

# Convert dictionary of dictionaries to a list of dictionaries
airport_list = [{"_id": code, **details} for code, details in data.items()]
total_no = len(airport_list)

# Insert the transformed data into MongoDB
try:
    print("inserting data into mongodb")
    collection.insert_many(airport_list, ordered=False)
    doc_count = collection.count_documents({})  # Count total documents in the collection
    print(f"Total number of documents in collection: {doc_count}")
    if doc_count == total_no:
        print("Data successfully inserted into MongoDB.")
    else:
        print("some inserts not successful, some duplicates exist")
except Exception as e:
    print(f"Error inserting data into MongoDB: {e}")
    
print("Closing the connection.")
try:
    client.close()
    print("Connection closed")
except Exception as e:
    print(f"Error closing connection: {e}")