import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
log = [0]*9
for i in range(n):
    t = input()
    for c in t:
        if c in '123456789':
            log[int(c)-1]+=1
            break
ben = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]
log = [100.0 * l / sum(log) for l in log]

diff = [abs(a-b) >= 10.0 for a,b in zip(log, ben)]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(any(diff)).lower())
