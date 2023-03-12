import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a1 = int(input())
n = int(input())
s=[str(a1)]
seen = {}
for i in range(n-1):
    last = s[-1]
    if last not in seen:
        s+=['0']
    else:
        s+=[str(i-seen[last])]
    seen[last] = i
print(s[-1])