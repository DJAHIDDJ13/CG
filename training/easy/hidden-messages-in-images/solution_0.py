import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
l=''
for i in range(h):
    for j in input().split():
        pixel = int(j)
        l+=bin(pixel)[-1]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(''.join([chr(int(l[i:i+8],2)) for i in range(0,len(l),8)]))
