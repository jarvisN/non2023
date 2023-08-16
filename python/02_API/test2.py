from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['testNon']

@app.route("/data", methods=['GET'])
def get_data():
    # Query data from MongoDB
    data = list(collection.find({}, {'_id': 0}))  # Exclude _id field from the response
    return jsonify(data)

@app.route("/test/<string:id>/<int:value>", methods=['POST'])
def post_data(id, value):
    # Create a new document and insert it into the MongoDB collection
    document = {"id": id, "value": value}
    collection.insert_one(document)
    return jsonify({"message": "Data posted successfully"})

if __name__ == "__main__":
    app.run()
