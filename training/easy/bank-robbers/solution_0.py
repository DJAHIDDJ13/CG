import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
v = int(input())
print(f'r: {r}, v: {v}', file=sys.stderr)
r_t = [0 for _ in range(r)]
for i in range(v):
    c, n = [int(j) for j in input().split()]
    r_t[r_t.index(min(r_t))] += (10**(n))*(5**(c-n))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(r_t, file=sys.stderr)
print(max(r_t))

