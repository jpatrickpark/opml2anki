# opml2anki

Turn an opml document into an anki deck. Every non-leaf node becomes a card.


## Example usage:

```bash
mkdir lab1
python create_deck.py data/lec1.opml > lec1/deck.md
ankdown -r lab1 -p lab1.apkg
```

## requirements

ankdown