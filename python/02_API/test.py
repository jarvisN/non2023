from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"lux": 123}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
