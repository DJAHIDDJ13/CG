import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()
bs = b.split('0')
m = -1
for s1,s2 in zip(bs[:],bs[1:]):
    if s1 != '' and s2 != '':
        m = len(s1)+len(s2)+1 if len(s1)+len(s2)+1 >m else m
f=list(filter(None, bs))
print(max(m,1 if len(f)==0 else max(map(len,f))+1))