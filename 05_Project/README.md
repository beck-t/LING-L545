# Cajun French Morphological Analyzer

Cajun French (CF, ISO-639-3 "frc") is an endangered language spoken primarily in south Louisiana. Multiple morphological analyzers have been created for Standard French, but none has ever focused on CF.

Using data from Indiana University Creole Institute's \emph{A la découverte du français cadien à travers la parole}, I developed a small finite-state transducer morphological analyzer for CF using the HFST lexc and twol formalisms.

The transducer is capable of analyzing thousands of words, including frequently ambiguous analyses. It analyzes hundreds of the most commonly-used words in the corpus, as well as less common words, though it has little support for non-derivational morphology. This is the first step towards a robust set of language tools for CF speakers.

# Compiling

Run `make` to compile the transducers (`frc.gen.hfst` and its inversion `frc.inv.hfst`). You may need to run `make clean` first.

# Examining the Files

- `adjectives.lexc` contains adjectives and nouns

- `verbs.lexc` contains verbs

- `misc.lexc` contains other syntactic categories

- `frc.twol` contains phonological rules