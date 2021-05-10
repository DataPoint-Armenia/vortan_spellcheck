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
        max_dictionary_edit_distance,
        prefix_length,
        unigram_freq_file, 
        bigram_freq_file = None,
    ):
        self.sym_spell = SymSpell(
            max_dictionary_edit_distance=max_dictionary_edit_distance,
            prefix_length=prefix_length,
        )

        self.sym_spell.load_dictionary(
            unigram_freq_file,
            term_index=0,
            count_index=1,
            encoding="utf-8",
        )
        
        if bigram_freq_file:
            self.sym_spell.load_bigram_dictionary(
                bigram_freq_file,
                term_index=0,
                count_index=2,
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

    def suggest_compound(
        self,
        phrase,
        max_edit_dist = None,
    ):
        if max_edit_dist == None:
            max_edit_dist = DEFAULT_MAX_EDIT_DISTANCE

        # spellcheck
        suggestions = self.sym_spell.lookup_compound(
            phrase,
            max_edit_distance=max_edit_dist,
            # ignore_non_words=False,
            # split_phrase_by_space=True,
        )
        return suggestions

