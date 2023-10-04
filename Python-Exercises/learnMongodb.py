import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
# Print current Mongo databases
# print(client.list_database_names())

# Choose or create a database and collection
mydb = client["testdb"]
collection = mydb["tfstateV3"]

with open("tfstate.json", "r") as json_file:
    data = json.load(json_file)

# Insert the JSON data into the collection
collection.insert_one(data)

# Close the MongoDB connection
client.close()

