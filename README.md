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

Create frequency dictionary from file of words:
```
python3 src/create_dict.py data/words.txt > data/freq.txt
```

Get spellcheck suggestions for word:
```
python3 src/spellcheck.py data/freq.txt ացուշ
անուշ, 1, 469
ապուշ, 1, 54
ացում, 1, 1
```

## Contributors

- [@sourenp](https://github.com/sourenp)

## Acknowledgements

- https://github.com/mammothb/symspellpy

