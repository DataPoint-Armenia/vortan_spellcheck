#!/usr/bin/python

import sys, os

sys.path.insert(0, './src/')
from spellcheck import spellchecker

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Բարեւ!'

@app.route('/suggest/<string:word>', methods=['GET'])
def suggest(word):
    response = {
        "word": word
    }
    suggestions = sp.suggest(word)
    response["suggestions"] = [s.term for s in suggestions]
    return jsonify(response), 201

if __name__ == '__main__':
    sp = spellchecker(
       corpus_path = sys.argv[1],
        max_dictionary_edit_distance = 2,
        prefix_length = 7,
    )
    app.run(debug=True)
