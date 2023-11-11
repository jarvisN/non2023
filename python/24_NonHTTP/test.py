from flask import Flask, request, jsonify
import random
import time
app = Flask(__name__)

# Define a route for handling HTTP GET requests
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/hand', methods=['GET'])
def get_random_int():
    random_int = random.randint(0, 5)
    
    # Create a dictionary to store the response
    response = {
        'button': random_int
    }
    
    # Return the response as JSON
    return jsonify(response)


def random_with_empty():
    value = random.randint(1, 5)
    is_empty = random.choice([True, False, False])
    return None if is_empty else value


@app.route('/hand2', methods=['GET'])
def get_random_int2():
    # random_int = random.randint(-20, 10)
    
    # print(random_int)
    # return str(random_int)
    
    result = random_with_empty()
    if result is None:
        return 'ค่าว่างเปล่า'
    return f'ค่าที่สุ่มได้: {result}'


@app.route('/force',methods=['GET'])
def test():
    return "2500:2500:2500:2500:2500:2500"


# Define a route for handling HTTP POST requests
@app.route('/echo', methods=['POST'])
def echo():
    # Get the JSON data from the request body
    data = request.get_json()

    if 'message' in data:
        message = data['message']
        return jsonify({'response': message})
    else:
        return jsonify({'error': 'No message provided'})
    
    
# Define a route for handling HTTP GET requests
@app.route('/non', methods=['POST'])
def non():
    data = request.args.get('data', default=None, type=str)
    print(data)
    return jsonify({'response': 'ok '})




if __name__ == '__main__':
    app.run(debug=True , port=8000)
