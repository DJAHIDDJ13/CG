import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

times = []
n = int(input())
for i in range(n):
    t = tuple(map(int, input().split(':')))
    times += [t]

fastest = min(times, key=lambda t:t[0] * 3600 + t[1] * 60 + t[2])
print("%02d:%02d:%02d" % fastest)