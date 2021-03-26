from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import query_engine

@app.route('/')
def hello_world():
    query = request.args.get('query')
    return {
        "data": query_engine.query(query)
    }