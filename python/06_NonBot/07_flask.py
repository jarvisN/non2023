from flask import Flask,jsonify,request

import socket

app = Flask(__name__)

deBug = []


@app.route("/")
def home():
    return "Hello, from Flask!"

@app.route('/myapi', methods=['POST'])
def myapi():
    data = request.get_json()
    print(data)
    # process the data as needed
    return 'Success'

if __name__ == "__main__":
    app.run()
