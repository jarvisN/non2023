from flask import Flask,jsonify
import json
from settingDB import ConnectionProvider
app = Flask(__name__)

deBug = []


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/test/create/<name>/<point>/<link>")
def testCreate(name,point,link):
    # add0 = "{:08d}".format(id)
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute(f"INSERT INTO allData (name , point , link) VALUES ('{name}', '{point}', '{link}')")
    conn.commit()
    mycursor.close()
    conn.close()

    return("Ok Done")

@app.route("/test/read")
def testRead():
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute("SELECT * FROM testNon")
    result_set = mycursor.fetchall()
    rows = [dict(zip([col[0] for col in mycursor.description], row)) for row in result_set]
    response = jsonify(rows)
    # Set the response headers to allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/test/find_point/<name>")
def find(name):
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute(f"SELECT * FROM allData WHERE name = '{name}'")
    result = mycursor.fetchall()
    return result


@app.route("/test/update/<id>/<name>")
def testUpdate(id,name):
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute(f"UPDATE testNon SET id = '{id}' WHERE name = '{name}'")
    conn.commit() 
    conn.close()
    return "Ok Updated"

@app.route("/test/delete/<name>")
def testDelete(name):
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute(f"DELETE FROM testNon WHERE name = '{name}'")
    conn.commit() 
    conn.close()
    return "Ok Deleted"


@app.route("/test/time/<name>/", defaults={ 'drt': None })
@app.route("/test/time/<name>/<drt>")
def testTime(name,drt):
    print(name)
    print(drt)
    return "ok"

@app.route("/test/read_table")
def readTable():
    conn = ConnectionProvider.myConnectionProvider()
    mycursor = conn.cursor(prepared=True)
    mycursor.execute("SELECT * FROM testNon")
    result_set = mycursor.fetchall()
    rows = [dict(zip([col[0] for col in mycursor.description], row))
            for row in result_set]
    response = jsonify(rows)

    # Set the response headers to allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response






if __name__ == "__main__":
    app.run()
