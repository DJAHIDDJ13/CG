import sys
import math
from pprint import pprint

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
n = int(input())
m=[]
robot = (0,0)
for i in range(h):
    line = input()
    if 'O' in line:
        robot = (line.index('O'),i,0)
    m+=[list(line)]

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
d = 0
seq = []
init = []
changed=False
for i in range(n):
    nx, ny = (robot[0]+dirs[d][0], robot[1]+dirs[d][1])
    while m[ny][nx] == '#':
        d = (d + 1)%4
        nx, ny = (robot[0]+dirs[d][0], robot[1]+dirs[d][1])
    if robot not in seq:
        seq+=[robot]
    else:
        changed=True
        idx = seq.index(robot)
        init = seq[:idx]
        seq = seq[idx:]
        break
    robot = (nx, ny, d)
if not changed:
    init, seq = seq+[robot], init

if n < len(init):
    robot = init[n]
else:
    robot = seq[(n-len(init))%len(seq)]
print(robot[0],robot[1])