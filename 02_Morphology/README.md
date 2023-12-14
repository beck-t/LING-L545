# Morphology: Latin Nouns

I built a morphological analyzer for the 20 most common nouns according to Dickinson College Commentaries' Core Vocabularies List (including *deus* and *dea* as separate nouns).

As far as I am aware, no productive derivations apply to these 20 nouns.

I created lexica for each of the 5 declensions, including multiple lexica for declensions that have multiple distinct ending patterns (e.g. separate lexica for masculine and neuter second-declension nouns).

There was also a separate "declension" included for the indeclinable noun *nihil*.

Third declension nouns have consistently irregular nominative singular forms, so they were defined a little differently than the rest. For example, *rēx, rēgis* was implemented as:

> rēx%<noun%>%<nom%>%<sg%>: rēx #;
> rēx%<noun%>: rēg N3-MF;

There were only a handful of relevant phonological processes here: the -er and -ir second-declension nouns and some variants of the fourth and fifth declensions.

