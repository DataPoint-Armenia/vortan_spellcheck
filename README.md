# vortan_spellcheck

## About

Spellcheck

## Documentation

- **Google Drive Folder**: [link](https://drive.google.com/drive/folders/1f1feyB_po6hS7TFvdvPWZ3Q6dSEDjklQ)
- **Slack Channel**: [#vortan](https://datapointarmenia.slack.com/archives/C01LE2ADLFJ)

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
```
python3 src/demo.py data/freq.txt
Initializing spellchecker...
Բարեւ
> ացուշ
անուշ, 1, 18000117
ապուշ, 1, 12305390
արուշ, 1, 23894
ացում, 1, 15929
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

