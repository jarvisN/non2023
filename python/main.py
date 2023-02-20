from flask import Flask,jsonify,request
import mariadb
import json
from settingDB import ConnectionProvider
import socket

app = Flask(__name__)

deBug = []


@app.route("/")
def home():
    return "Hello, from Flask!"


@app.route("/test/<id>/<name>")
def testsendData(id,name):

    # add0 = "{:08d}".format(id)

    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute(f"INSERT INTO testNon (id, name) VALUES ('{id}', '{name}')")
    conn.commit()
    mycursor.close()
    conn.close()

    return("Ok Done")

@app.route("/test/read_table")
def readTable():
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute("SELECT * FROM testNon")
    result_set = mycursor.fetchall()
    rows = [dict(zip([col[0] for col in mycursor.description], row)) for row in result_set]
    response = jsonify(rows)
    
    # Set the response headers to allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/test/createdb/<string:data>/")
def testCreateDB(data):
    conn = ConnectionProvider.myConnectionProvider()
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {data}")
     # Get query results and return response
    try:
        result = cur.fetchall()
        return jsonify(result)
    except mariadb.ProgrammingError:
        # Handle error and send error response
        error_message = "Error executing query: no result set"
        response = jsonify({"error": error_message})
        response.status_code = 400  # Bad Request
        return response





@app.route('/zumi/<string:test>', methods=['GET'])
def hello(test):

    TCP_IP = '127.0.0.1'
    TCP_PORT = 6999
    MESSAGE = "test from flask"

    print("TCP target IP:", TCP_IP)
    print("TCP target port:", TCP_PORT)
    print("message:", MESSAGE)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    sock.sendall(MESSAGE.encode())
    sock.close()

    return "Ok Show on Dashboard"


if __name__ == "__main__":
    app.run()
