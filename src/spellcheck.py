#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import pkg_resources
from symspellpy import SymSpell, Verbosity
from itertools import islice
import sys

DEFAULT_MAX_EDIT_DISTANCE = 2

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
        max_edit_dist = None,
        include_unknown=True,
        verbosity = Verbosity.CLOSEST,
    ):
        # defaults
        if max_edit_dist == None:
            max_edit_dist = DEFAULT_MAX_EDIT_DISTANCE

        # spellcheck
        suggestions = self.sym_spell.lookup(
            word,
            verbosity,
            max_edit_distance=max_edit_dist,
            include_unknown=include_unknown,
        )
        return suggestions
