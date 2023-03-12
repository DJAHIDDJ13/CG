import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
maps = []
n = int(input())
for i in range(n):
    maps += [[]]
    for _ in range(h):
        maps[-1] += [list(input())]

def cost(m, x, y):
    length = 1
    moves = {'>':(1,0),'<':(-1,0),'^':(0,-1),'v':(0,1)}
    try:
        while m[x][y] in ['<','>','^','v'] and length <= 20*20:
            my, mx = moves[m[x][y]]
            x, y = x+mx, y+my
            length += 1
    except:
        return -1
    if m[x][y] == 'T':
        return length
    else:
        return -1
v = -1
vi = -1
for i in range(n):
    nc = cost(maps[i], start_row, start_col)
    if (nc < v or v == -1) and nc != -1:
        v = nc
        vi = i
print(vi if v != -1 else 'TRAP')