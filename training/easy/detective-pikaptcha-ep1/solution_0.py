import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
a = []
for i in range(height):
    line = input()
    a += [list(line)]
for i in range(height):
    for j in range(width):
        if a[i][j] != '#':
            a[i][j] = int(a[i][j])
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<height and 0<=y<width:
                    if a[x][y] != '#':
                        a[i][j] += 1
for l in a:
    print(*l, sep='')