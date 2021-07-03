import sys
import os

sys.path.insert(0, './src/')

from spellcheck import spellchecker


print("Initializing spellchecker...")

sp = spellchecker(
    max_dictionary_edit_distance = 2,
    prefix_length = 7,
    unigram_freq_file = sys.argv[1],
    bigram_freq_file = sys.argv[2] if len(sys.argv) == 3 else None,
)

sp.sym_spell.save_pickle(sys.argv[3])
print("Saved pickle to " + sys.argv[3])
