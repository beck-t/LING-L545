# Disambiguation: Constraint Grammar

I added five rules to the Constraint Grammar:

> `REMOVE VPLURAL IF (-1C PNSING);`
> `REMOVE VSING IF (-1C PNPLURAL);`

> `REMOVE V1P IF ((-1C PN2P) or (-1C PN3P));`
> `REMOVE V2P IF ((-1C PN3P) or (-1C PN1P));`
> `REMOVE V3P IF ((-1C PN1P) or (-1C PN2P));`

These are all designed to disambiguate between ambiguous verb forms based on a preceding nominative case pronoun. The first two rules rule out numbers contradicted by the pronoun, and the last three eliminate persons contradicted.

To run:

> `python3 ud-scripts/conllu-analyser.py eng-analyser.tsv < input.txt | vislcg3 --trace --grammar eng.cg3'