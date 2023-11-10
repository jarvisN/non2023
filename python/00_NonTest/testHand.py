from flask import Flask, jsonify
import random

app = Flask(__name__)

# Define a route for handling HTTP GET requests
@app.route('/get_random_int', methods=['GET'])
def get_random_int():
    # Generate a random integer between 1 and 100 (inclusive)
    random_int = random.randint(1, 100)
    
    # Create a dictionary to store the response
    response = {
        'random_int': random_int
    }
    
    # Return the response as JSON
    return jsonify(response)


@app.route('/hand2', methods=['GET'])
def test2():
    # Generate a random integer between 1 and 100 (inclusive)
    random_int = random.randint(1, 70)
    
    return str(random_int)
    
if __name__ == '__main__':
    app.run(debug=True)
