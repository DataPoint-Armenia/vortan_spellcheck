#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import sys
import os
import pprint

sys.path.insert(0, './src/')

from spellcheck import spellchecker


print("Initializing spellchecker...")

pp = pprint.PrettyPrinter(indent=2)

sp = spellchecker(
    max_dictionary_edit_distance = 2,
    prefix_length = 7,
    unigram_freq_file = sys.argv[1] if len(sys.argv) <= 3 else None,
    bigram_freq_file = sys.argv[2] if len(sys.argv) == 3 else None,
    pickle_file = sys.argv[3] if len(sys.argv) == 4 else None,
)

print("Բարեւ")

while True:
    try:
        phrase = input('> ')
        if len(phrase.split(' ')) <= 1:
            result = sp.suggest(phrase)
            result['suggestions'] = [str(x) for x in result['suggestions']]
            for s in result['suggestions']:
                pp.pprint(s)
        else:
            sentence_results = sp.suggest_tokenize(phrase)
            for result in sentence_results:
                result['suggestions'] = [str(x) for x in result['suggestions']]
                pp.pprint(result)
    
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

