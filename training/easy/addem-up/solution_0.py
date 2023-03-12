import sys
import math
import bisect
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in input().split():
    x = int(i)
    bisect.insort(a,x)
cost = 0
while len(a) > 2:
    x, y, *t = a
    a = t
    bisect.insort(a, x+y)
    cost += x+y
print(cost+sum(a))
