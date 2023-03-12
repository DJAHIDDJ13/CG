import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

lines = []

for i in range(h):
    lines += [input()]

names = list(filter(None, lines[0].split()))
nums = list(filter(None, lines[-1].split()))

ends = [[names[i]] for i in range(len(names))]
for i in range(1, h-1):
    line = lines[i]
    
    for idx in range(len(names)-1):
        if line[idx*3+1] == '-':
            temp = ends[idx]
            ends[idx] = ends[idx+1]
            ends[idx+1] = temp


res = {}
for idx, arr in enumerate(ends):
    for i in arr:
        if i != []:
            res[i] = f"{i}{nums[idx]}"

for i in names:
    print(res[i])

