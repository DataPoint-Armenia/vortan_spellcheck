#!/usr/bin/python

import sys, os

sys.path.insert(0, './src/')
from spellcheck import spellchecker

from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'Բարեւ!'

@app.route('/suggest', methods=['POST'])
def suggest():
    word = request.get_json()["word"]
    # query params
    params = _parse_args(request)

    # spellcheck
    suggestions = sp.suggest(
        word=word,
        max_edit_dist=params['max_edit_dist'],
    )

    # response
    response = {
        "input": word
    }
    response["suggestions"] = [s.term for s in suggestions]
    return jsonify(response), 201

def _parse_args(request):
    max_edit_dist_arg = request.args.get('max_edit_distance')
    return {
        'max_edit_dist': int(max_edit_dist_arg) if max_edit_dist_arg else None
    }

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Loading spellchecker...")
    sp = spellchecker(
       corpus_path = sys.argv[1],
        max_dictionary_edit_distance = 2,
        prefix_length = 7,
    )
    print("Done.")

    app.run(debug=True)
