# vortan_spellcheck

## About

MVP spellcheck implementation

## Documentation

- [vortan_docs](https://github.com/DataPoint-Armenia/vortan_docs)

### Prereqs

- [python](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)

### Installation

1. Clone the repo
```
git clone git@github.com:DataPoint-Armenia/vortan_spellcheck.git
```
2. Install requirements
```
pip3 install -r requirements.txt
```

## Usage

As a module
```python3
from spellcheck import spellchecker

sp = spellchecker(
    max_dictionary_edit_distance = 2,
    prefix_length = 7,
    unigram_freq_file = "uni.txt"
    bigram_freq_file = "bi.txt"
)

for s in sp.suggest("տպրոց"):
    print(s)
```

Spellcheck demo
```bash
# unigram
➜ python3 demo/demo.py data/uni_freq.txt
Initializing spellchecker...
Բարեւ
> տպրոց
դպրոց, 1, 1

# bigram
➜ python3 demo/demo.py data/uni_freq.txt data/bi_freq.tx
Initializing spellchecker...
Բարեւ
> Քնացի տպրոց՝ ուղագրություն սուորելու:  
գնացի դպրոց ուշադրություն սովորելու, 7, 0
```

Symspell pickle creation
```
python3 src/pickle_dict.py data/uni_freq.txt data/bi_freq.txt data/symspell_dict.pickle
```

Dictionary creation
```
python3 src/create_dict.py data/words.txt > data/freq.txt
```

## Contributors

- [@sourencho](https://github.com/sourencho)

## Acknowledgements

- https://github.com/mammothb/symspellpy
