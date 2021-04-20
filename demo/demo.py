#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import sys
import os

sys.path.insert(0, './src/')

from spellcheck import spellchecker


print("Initializing spellchecker...")

sp = spellchecker(
   corpus_path = sys.argv[1],
    max_dictionary_edit_distance = 2,
    prefix_length = 7,
)

print("Բարեւ")

while True:
    try:
        word = input('> ')
        for suggestion in sp.suggest(word):
            print(suggestion)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

