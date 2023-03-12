import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, count_x, count_y = [int(i) for i in input().split()]
l1=[]
f=[0]
for i in input().split():
    x = int(i)
    for z in f:
        l1 += [x-z]
    f+=[x]
for z in f:
    l1 += [w-z]

l2=[]
f=[0]
for i in input().split():
    y = int(i)
    for z in f:
        l2 += [y-z]
    f+=[y]

for z in f:
    l2 += [h-z]


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
s=0
for x in l1:
    s += l2.count(x)
print(s)
