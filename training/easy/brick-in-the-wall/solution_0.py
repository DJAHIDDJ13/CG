import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
n = int(input())
bricks = []
for i in input().split():
    m = int(i)
    bricks += [m]

bricks = sorted(bricks, reverse=True)
bricks = [bricks[i:i+x] for i in range(0, n, x)]
g = 10.0
work = sum([L * 6.5 / 100 * g * sum(row) for L, row in enumerate(bricks)])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("%.3f" % work)
