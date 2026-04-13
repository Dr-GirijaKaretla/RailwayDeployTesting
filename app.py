from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Railway!"})

@app.route('/api/hello/<name>')
def hello_name(name):
    return jsonify({"message": f"Hello, {name}!"})

