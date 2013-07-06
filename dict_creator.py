#!/usr/bin/env python

f = open('/usr/share/dict/words')
d = {}
lets = set('abcdefghijklmnopqrstuvwxyz\n')
for word in f:
  if len(set(word) - lets) == 0 and len(word) > 2 and len(word) < 9:
    word = word.strip()
    key = ''.join(sorted(word))
    if key in d:
      d[key].append(word)
    else:
      d[key] = [word]
f.close()
anadict = [' '.join([key]+value) for key, value in d.iteritems()]
anadict.sort()
f = open('anadict.txt','w')
f.write('\n'.join(anadict))
f.close()