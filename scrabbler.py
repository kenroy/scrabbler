#!/usr/bin/env python

from itertools import combinations
from time import time
import collections

def load_anagrams():
    ''' (file) -> dict {str:[list of str]}
    Returns a collections.defaultdict of anagrams.
    '''
    anagrams = collections.defaultdict(list)

    with open('anasowpods.txt', 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            anagrams[tuple(words[0])] = words[1:]

    return anagrams

scores = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}

def score_word(word):
    ''' (str) -> int
    Returns total score of word.
    '''
    return sum([scores[c] for c in word])

def findwords(rack, anagrams):
    ''' (str, defaultdict) -> [list of str]
    Returns all possible words found from given letters.
    '''
    rack = ''.join(sorted(rack))
    foundwords = []

    for i in xrange(2, len(rack) + 1):
        for combination in combinations(rack, i):
            if combination in anagrams:
                foundwords.extend(anagrams[combination])

    return foundwords

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        rack = sys.argv[1].strip()
    else:
        print "Usage: " + sys.argv[0] + " <yourrack>"
        exit()

    t = time()
    anagrams = load_anagrams()
    print "Dictionary loading time:", (time() - t)
    t = time()
    foundwords = set(findwords(rack, anagrams))
    scored = [(score_word(word), word) for word in foundwords]
    scored.sort()

    for score, word in scored:
        print "%d\t%s" % (score, word)

    print "Time elapsed:", (time() - t)
