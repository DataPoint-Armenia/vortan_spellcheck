from symspellpy import SymSpell, Verbosity

sym_spell = SymSpell()
corpus_path = "data/words.txt"
sym_spell.create_dictionary(corpus_path, encoding='utf-8')

input_term = "ացուշ"

suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST,
                               max_edit_distance=2, include_unknown=True)

for suggestion in suggestions:
    print(suggestion)
