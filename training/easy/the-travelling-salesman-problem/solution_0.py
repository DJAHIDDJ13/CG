import sys
import math
from itertools import permutations
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
a=[]
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    a += [(x, y)]

pathlen = 0
cur = 0
seen = [False] * n
seen[0] = True
for i in range(n-1):
    x, y = a[cur]
    cur = min([(a[j], j) for j in range(n) if not seen[j]], key=lambda v:(v[0][0]-x)**2+(v[0][1]-y)**2)[1]
    seen[cur] = True
    pathlen += ((x-a[cur][0])**2 + (y-a[cur][1])**2)**.5
pathlen += ((a[0][0]-a[cur][0])**2 + (a[0][1]-a[cur][1])**2)**.5
print(round(pathlen))