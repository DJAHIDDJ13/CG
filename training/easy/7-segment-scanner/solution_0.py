import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line_1 = input()
line_2 = input()
line_3 = input()

l1 = [line_1[i:i+3] for i in range(0,len(line_1),3)]
l2 = [line_2[i:i+3] for i in range(0,len(line_2),3)]
l3 = [line_3[i:i+3] for i in range(0,len(line_3),3)]
a = [l1[i]+l2[i]+l3[i] for i in range(len(l1))]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
lookup = [' _ | ||_|', '     |  |', ' _  _||_ ', ' _  _| _|', '   |_|  |', ' _ |_  _|', ' _ |_ |_|', ' _   |  |', ' _ |_||_|', ' _ |_| _|']

print(''.join([str(lookup.index(a[i])) for i in range(len(a))]))
