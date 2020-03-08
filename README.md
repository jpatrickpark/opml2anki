# opml2anki

Turn an opml document into an anki deck. Every non-leaf node becomes a card.


## Example usage:

To create lab1.apkg using data/lec1.opml, run the following:

```bash
python create_deck.py data/lec1.opml
```
It creates lec1/deck.md file as an intermediate upon which ankdown is called.

## requirements

ankdown
argparse