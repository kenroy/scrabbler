#!/usr/bin/env python

from bisect import bisect_left
from itertools import combinations
from time import time

def loadvars():
  f = open('anadict.txt','r')
  anadict = f.read().split('\n')
  f.close()
  return anadict

scores = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}

def score_word(word):
  return sum([scores[c] for c in word])

def findwords(rack, anadict):
  rack = ''.join(sorted(rack))
  foundwords = []
  for i in xrange(2,len(rack)+1):
    for comb in combinations(rack,i):
      ana = ''.join(comb)
      j = bisect_left(anadict, ana)
      if j == len(anadict):
        continue
      words = anadict[j].split()
      if words[0] == ana:
        foundwords.extend(words[1:])
  return foundwords

if __name__ == "__main__":
  import sys
  if len(sys.argv) == 2:
    rack = sys.argv[1].strip()
  else:
    print "Usage: " + sys.argv[0] + " <yourrack>"
    exit()
  t = time()
  anadict = loadvars()
  print "Dictionary loading time:",(time()-t)
  t = time()
  foundwords = set(findwords(rack, anadict))
  scored = [(score_word(word), word) for word in foundwords]
  scored.sort()
  for score, word in scored:
    print "%d\t%s" % (score,word)
  print "Time elapsed:", (time()-t)