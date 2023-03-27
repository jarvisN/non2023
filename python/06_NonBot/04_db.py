import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NonBot"]

# Create a collection
collection = db["test"]

# # Insert a document into the collection
# data = {"user": "1", "data1": 567}
# collection.insert_one(data)

# # Find a document in the collection
# query = {"user": "1"}
# data = collection.find(query)
# for document in data:
#     print(document)

# # Find the last document in the collection based on the insertion order (_id)
# last_document = collection.find_one(sort=[("_id", pymongo.DESCENDING)])
# # Print the last document
# print(last_document)

# # Find the last two documents in the collection
# cursor = collection.find().sort([("_id", -1)]).limit(2)
# # Convert the cursor to a list
# documents = list(cursor)
# print(documents)



print("\n ================================================= \n")

