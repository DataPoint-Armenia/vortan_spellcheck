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

API
```
python3 api/app.py data/freq.txt
curl -X POST -H "Content-Type: application/json;" -s http://127.0.0.1:5000/suggest -d '{"word": "ացուշ"}'
```

## Helpful commands

Curl api, pull out first suggestion and decode to utf-8
```
curl -X POST -H "Content-Type: application/json;" -s http://127.0.0.1:5000/suggest -d '{"word": "ացուշ"}' | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['suggestions'][0].encode('latin1').decode('utf8'))"
```

## Contributors

- [@sourencho](https://github.com/sourencho)

## Acknowledgements

- https://github.com/mammothb/symspellpy

