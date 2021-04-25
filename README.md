# vortan_spellcheck

## About

Spellcheck

## Documentation

- **Technical Spec**: [link](https://docs.google.com/document/d/174XceYg-MSX32kfEz-C4bQx8zk43uHebvGSBaEduQWM/edit)
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
// Open your browser and go to http://127.0.0.1:5000/suggest/ացուշ
```

## Contributors

- [@sourenp](https://github.com/sourenp)

## Acknowledgements

- https://github.com/mammothb/symspellpy

