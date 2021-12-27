#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import pkg_resources
from symspellpy import SymSpell, Verbosity
from itertools import islice
import sys
import sqlite3
from typing import List

#extern
sys.path.insert(0, 'extern/vortan_tokenizer/')
from tokenizer import VortanTokenizer

DEFAULT_MAX_EDIT_DISTANCE = 2


def tokenize_sentence(text: str) -> List[str]:
    T = VortanTokenizer(text)
    T.add_segment(text).tokenization()
    for s in T.segments:
        sentence = []
        for index, t in enumerate(s['tokens']):
            w = t[1] if index != 0 else t[1].lower()
            sentence.append(w)
        return sentence # just first sentence


class spellchecker:
    def __init__(
        self,
        max_dictionary_edit_distance,
        prefix_length,
        unigram_freq_file, 
        bigram_freq_file = None,
        pickle_file = None,
    ):
        self.sym_spell = SymSpell(
            max_dictionary_edit_distance=max_dictionary_edit_distance,
            prefix_length=prefix_length,
        )

        if pickle_file is not None:
            self.sym_spell.load_pickle(
                pickle_file,
            )
        else:
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
        return {
            'original_term': word,
            'suggestions': suggestions,
        }

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

    def tokenize(self, phrases):
        return tokenize_sentence(phrases)

    # Tokenize into individual phrases and return a list of suggestions for each 
    def suggest_tokenize(
        self,
        phrases,
        max_edit_dist = None,
        include_unknown=True,
        verbosity = Verbosity.CLOSEST,
    ):
        if max_edit_dist == None:
            max_edit_dist = DEFAULT_MAX_EDIT_DISTANCE

        words = self.tokenize(phrases)

        sentence_suggestions = []
        for word in words:
            suggestions = self.sym_spell.lookup(
                word,
                verbosity,
                max_edit_distance=max_edit_dist,
                include_unknown=include_unknown,
            )
            sentence_suggestions.append({
                'original_term': word,
                'suggestions': suggestions,
            })

        return sentence_suggestions
