#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import pkg_resources
from symspellpy import SymSpell, Verbosity
from itertools import islice
import sys

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
corpus_path = sys.argv[1]

# term_index is the column of the term and count_index is the
# column of the term frequency
success = sym_spell.load_dictionary(corpus_path, term_index=0, count_index=1, encoding="utf-8")

# lookup suggestions for single-word input strings
input_term = sys.argv[2]

# max edit distance per lookup
# (max_edit_distance_lookup <= max_dictionary_edit_distance)
suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST,
                               max_edit_distance=2)
# display suggestion term, term frequency, and edit distance
for suggestion in suggestions:
    print(suggestion)
