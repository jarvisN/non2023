from flask import Flask
from settingDB import ConnectionProvider
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

@app.route("/test/<name>/<time>")
def test(name,time):

    return name

@app.route("/test/create/<name>/<time>")
def testCreate(name,time):
    conn = ConnectionProvider.myConnectionProvider()
    mycursor=conn.cursor(prepared=True)
    mycursor.execute(f"INSERT INTO testDB (name, time) VALUES ('{name}', '{time}')")
    conn.commit()
    mycursor.close()
    conn.close()

    return("Ok Done")

if __name__ == "__main__":
    app.run()
