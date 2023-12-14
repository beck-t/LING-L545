# Tokenization: PySBD Report

I used the Python Sentence Boundary Disambiguation (PySBD) by Nipun Sadvilkar and Mark Neumann. This is a Python project based on the Pragmatic Segmenter by Kevin S. Dias, which was written in Ruby. PySBD is a rule-based segmenter that does not use machine learning and makes extensive use of regexes, with rules for 22 languages; Old English is not one of them. Still, most of the sentence boundary issues are the same as in modern English, so I used that setting.

I expect it to be thrown off by abbreviations that differ between the two languages, but none were in my sample, which was randomly selected using Random.org's random integer generator. Unfortunately, the randomly selected paragraphs are mostly stub articles that don't pose too many complicated issues.

There were a total of 54 sentences in the sample, or 53 sentence boundaries. Of these, only one was detected incorrectly, so its accuracy was 98%.

It did not detect a sentence boundary at a semicolon, which was interesting behavior. However, the semicolon preceded a list, so it was correct. It also properly handled colons, parentheses, and <> brackets. The only error was in an article about a sports team from Washington, D.C., where "Washington D.C." was at the end of a sentence. In this case, the segmenter did not segment the sentences because of the abbreviation. Overall, it seems highly accurate, but stumbles when abbreviations are at the end of words, assuming abbreviations will never be a sentence boundary. This is not a major problem for Old English, as most of the abbreviations used on Old English Wikipedia are loans from other languages. But for those other languages, this can pose a serious issue.

# Segmentation: Maxmatch Implementation

To use my implementation of maxmatch, run `python3 maxmatch.py`. It expects two files, `dictionary.txt` (a dictionary file of segmented surface forms) and `test.conllu`. I have included these files in the repository.

Note that my implementation requires the `pyconll` Python package.

This implementation works well until it encounters a word that is not in its dictionary at all. Once it encountered a completely unknown token, everything else in the sentence would be messed up.

In earlier iterations, this was very common with punctuation marks, so I added the comma and quotation marks to the dictionary manually in the hopes that this would help.

Before this addition, the WER was about 1%; now it's lower, with a 0.59% WER.