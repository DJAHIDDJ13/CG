import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words=[]
maxlen = 0
for i in range(n):
    word = input()
    words += [word]
    maxlen = max(maxlen, len(word))
prefixes = ['' for w in words]
done = [False] * len(words)
for i in range(maxlen):
    new_pref = [prefixes[j]+words[j][i] if i < len(words[j]) else prefixes[j] for j,p in enumerate(words)]
    prefs = []
    k=0
    for p,n in zip(prefixes,new_pref):
        if new_pref.count(n) > 1 or p == '' and done[k]:
            prefs += [n]
        else:
            if not done[k]:
                prefs += [n]
            else:
                prefs += [p]
            done[k]=True
        k+=1
    prefixes = prefs
print('\n'.join(prefixes))