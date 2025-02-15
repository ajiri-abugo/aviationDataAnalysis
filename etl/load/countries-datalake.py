import sys
import os
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../../"))
from config.mongoconnect import get_mongo_db  # Import the connection function

# Get MongoDB database
db, client = get_mongo_db()

# Select database and collection
collection = db["countries"]

# Path to the JSON file
json_file_path = "/home/ajiri/project/aviationDataAnalysis/data/raw/countries.json"

# Initialize line counter
line_count = 0

# Open the file and count lines
with open(json_file_path, "r") as file:
    for line in file:
        line_count += 1
print(f"The JSON file has {line_count} lines.")


# Insert data (handling line-separated JSON)
with open(json_file_path, "r") as file:
    for line in file:
        try:
            document = json.loads(line)  # Read each line as a separate JSON document
            collection.insert_one(document)  # Insert into MongoDB
            doc_count = collection.count_documents({})  # Count total documents in the collection
            #print(f"Total number of documents in collection: {doc_count}")
            if doc_count == line_count:
                print("Data successfully inserted into MongoDB.")
        except json.JSONDecodeError as e:
            print(f"Skipping invalid JSON line: {line} - Error: {e}")

print("Closing the connection.")
try:
    client.close()
    print("Connection closed")
except Exception as e:
    print(f"Error closing connection: {e}")