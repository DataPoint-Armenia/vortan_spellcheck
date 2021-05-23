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
    phrase = request.get_json()["word"]
    # query params
    params = _parse_args(request)

    # spellcheck
    if len(phrase.split(' ')) <= 1:
        suggestions = sp.suggest(
            phrase,
            max_edit_dist=params['max_edit_dist'],
        )
    else:
        suggestions = sp.suggest_compound(
            phrase,
            max_edit_dist=params['max_edit_dist'],
        )

    # response
    response = {
        "input": phrase
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
    print(e)
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Loading spellchecker...")
    sp = spellchecker(
        max_dictionary_edit_distance = 2,
        prefix_length = 7,
        unigram_freq_file = sys.argv[1],
        bigram_freq_file = sys.argv[2] if len(sys.argv) == 3 else None,
    )
    print("Done.")

    app.run(debug=True)
