#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import pkg_resources
from symspellpy import SymSpell, Verbosity
from itertools import islice
import sys

class spellchecker:
    def __init__(
        self,
        corpus_path,
        max_dictionary_edit_distance,
        prefix_length,
    ):
        self.sym_spell = SymSpell(
            max_dictionary_edit_distance=max_dictionary_edit_distance,
            prefix_length=prefix_length,
        )

        self.sym_spell.load_dictionary(
            corpus_path,
            term_index=0,
            count_index=1,
            encoding="utf-8",
        )

    def suggest(
        self,
        word,
        verbosity = Verbosity.CLOSEST,
        max_edit_distance = 2,
    ):
        suggestions = self.sym_spell.lookup(
            word,
            verbosity,
            max_edit_distance=max_edit_distance
        )
        return suggestions
