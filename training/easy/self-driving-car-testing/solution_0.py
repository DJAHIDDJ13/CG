import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
x, *commands = input().split(';')
x = int(x)
full_commands = []
for c in commands:
    full_commands += [c[-1] for _ in range(int(c[:-1]))]

road = []
for i in range(n):
    r, roadpattern = input().split(';')
    r = int(r)
    road += [list(roadpattern) for _ in range(r)]

for i in range(len(road)):
    x += {'R':1, 'L':-1, 'S':0}[full_commands[i]]
    road[i][x-1] = '#'
print(*map(lambda l:''.join(l), road), sep='\n')