from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

import query_engine

@app.route('/query')
def get_query_results():
    query = request.args.get('query')
    query, search_words = query_engine.query(query)
    return {
        "results": query,
        "search_words": search_words
    }

@app.route('/document')
def get_document():
    doc_id = request.args.get('doc_id')
    doc = None
    with open('./ShortStories/{doc_id}.txt'.format(doc_id = doc_id)) as f:
        doc_name = f.readline().strip()
        doc = f.read()

    return {
        "doc_name": doc_name,
        "doc": doc
    }

@app.route('/doc_index')
def get_doc_index():
    doc_index = {}
    with open('./doc_index.json', 'r') as file:
        doc_index = json.load(file)

    return doc_index