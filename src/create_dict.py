from symspellpy import SymSpell
import sys

sym_spell = SymSpell()
corpus_path = sys.argv[1]
sym_spell.create_dictionary(corpus_path, encoding='utf-8')

for key, value in sym_spell.words.items():
    print("{0} {1}".format(key, value))
