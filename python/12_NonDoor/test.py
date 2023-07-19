from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def receive_data():
    data = request.form.get('data')
    if data:
        # Do something with the received data
        return 'Data received: ' + data
    else:
        return 'No data received.'

if __name__ == '__main__':
    app.run()
