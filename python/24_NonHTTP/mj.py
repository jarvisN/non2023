from flask import Flask

app = Flask(__name__)

@app.route('/mj')
def mj():
    return 'Robotlab'

@app.route('/non' )
def non():
    return 'a'

if __name__ == '__main__':
    app.run(debug=True,port=2222,host='172.20.10.11 ')
