#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.logs
collection = db.nginx

# Get the total number of logs
total_logs = collection.count_documents({})

# Display the total number of logs
print(f"{total_logs} logs")

# Display the count for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\t{count} {method} logs")

# Display the count for a specific method and path
specific_method = "GET"
specific_path = "/status"
count = collection.count_documents({"method": specific_method, "path": specific_path})
print(f"{count} logs with method={specific_method} and path={specific_path}")

