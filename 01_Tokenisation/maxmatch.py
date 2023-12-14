import pyconll

# The dictionary was generated from the training data using a script I wrote
# And then preprocessed so that this script can accept it as input with minimal pain

def maxmatch(t, dictionary):
    if t is not None:
        # python is weird about defining decrement loops so we have to do this
        for i in range(len(t)-1,0,-1):
            first_word = t[0:i]
            remainder = t[i:len(t)]
            if first_word in dictionary:
                if first_word != t:
                    return first_word + " " + maxmatch(remainder, dictionary)
                return first_word + " "
        return t + " "
    return ""

def ref_sentence(s):
    r = ""
    for token in s:
        r += token.form + " "
    return r
        
def main():
    trainfile = open('dictionary.txt','r')
    testiter = pyconll.load.iter_from_file('test.conllu')

    dict = trainfile.readline().split(',')
    dict += [',','“','”']
    output = ""
    reference = ""

    for sentence in testiter:
        reference += ref_sentence(sentence) + "\n"
        output += maxmatch(sentence.text, dict) + "\n"
        
    results = open('result.txt','w')
    ref_file = open('reference.txt','w')
    results.write(output)
    ref_file.write(reference)

main()