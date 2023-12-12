# Beck Tabor
# LING 545
# Modified 12/5/2023

import pyconll
import sys
import matplotlib.pyplot as plt

# adapted from code by Francis Tyers
def plot(labels, x, y, filename):
    # x = proportion OV, y = proportion V)
    plt.plot(x, y, 'ro')
    plt.title('Relative word order of verb and object')
    plt.xlim([0,1]) # Set the x and y axis ranges
    plt.ylim([0,1])
    plt.xlabel('OV') # Set the x and y axis labels
    plt.ylabel('VO')
    for i in range(len(labels)):  # Add labels to each of the points
        plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
    plt.savefig(filename)
    plt.show()

def word_order(iter):
    count = 0 # total occurrences, VO and OV
    ov = 0 # the number of object-verb occurrences
    for sentence in iter:
        for token in sentence:
            t = token.conll().split("\t")
            if t[7] == 'obj':
                head = sentence[t[6]].conll().split('\t')
                if head[3] == 'VERB':
                    if head[0] > t[0]:
                        ov = ov + 1
                    count = count + 1
    return ov*1.0/count
 
def main():
    ar = 'ar.conllu'
    zh = 'zh.conllu'
    en = 'en.conllu'
    fr = 'fr.conllu'
    ja = 'ja.conllu'
    la = 'la.conllu'
    pt = 'pt.conllu'
    ru = 'ru.conllu'
    gd = 'gd.conllu'
    ur = 'ur.conllu'
    
    langs = ['ar', 'zh', 'en', 'fr', 'ja', 'la', 'pt', 'ru', 'gd', 'ur']
    x = []
    y = []

    # Run word_order on each of the files and add the output to x
    # and 1-x to y
    x.append(word_order(pyconll.load.iter_from_file(ar)))
    y.append(1.0-x[0])
    x.append(word_order(pyconll.load.iter_from_file(zh)))
    y.append(1.0-x[1])
    x.append(word_order(pyconll.load.iter_from_file(en)))
    y.append(1.0-x[2])
    x.append(word_order(pyconll.load.iter_from_file(fr)))
    y.append(1.0-x[3])
    x.append(word_order(pyconll.load.iter_from_file(ja)))
    y.append(1.0-x[4])
    x.append(word_order(pyconll.load.iter_from_file(la)))
    y.append(1.0-x[5])
    x.append(word_order(pyconll.load.iter_from_file(pt)))
    y.append(1.0-x[6])
    x.append(word_order(pyconll.load.iter_from_file(ru)))
    y.append(1.0-x[7])
    x.append(word_order(pyconll.load.iter_from_file(gd)))
    y.append(1.0-x[8])
    x.append(word_order(pyconll.load.iter_from_file(ur)))
    y.append(1.0-x[9])
    
    print(x)
    print(y)
    plot(langs, x, y, "parsing.png")

main()