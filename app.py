from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Endpoint 1: Root endpoint
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

# Endpoint 2: Greet a user
@app.route('/greet/<string:name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Endpoint 3: Add two numbers
@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2
    return jsonify({"result": result})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)