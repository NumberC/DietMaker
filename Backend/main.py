import json
from flask import Flask, jsonify, request
import requests

import math

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run()

@app.route('/', methods=['POST'])
def query_records():
    print(request.data)
    data = json.loads(request.data)
    height = data['height']
    weight = data['weight']
    age = data['age']
    sex = data['sex']
    dietaryRestrictions = data['dietaryRestrictions']

    print("height: " + height)
    print("weight: " + weight)
    print("age: " + age)
    print("sex: " + sex)
    print("dietary restrictions: " + dietaryRestrictions)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
