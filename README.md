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

Dictionary creation
```
python3 src/create_dict.py data/words.txt > data/freq.txt
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

## Contributors

- [@sourencho](https://github.com/sourencho)

## Acknowledgements

- https://github.com/mammothb/symspellpy
