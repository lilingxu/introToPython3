#wordfreq.py
'Use github to do SVC'
'Use command line to commit'
"""
Write a program that analyzes text documents
and counts how many times each word appears in the documents
"""
def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words. \n")

    # get the sequence of words from the file
    fname = input("File to analyze: ")
    text = open(fname,'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,_./:;':
        text = text.replace(ch, ' ')
        words = text.split()

    # construct dictionary of word counts
    counts = {}
    for w in words:
        # if w is not already in the dictionary, this get will return 0
        counts[w] = counts.get(w,0) + 1
    
    # output analysis of n most frequent words
    n = eval(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()                         # order by alphabetically
    items.sort(key=byFreq, reverse=True) # orders by frequency
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

if __name__ == '__main__':
    main()
