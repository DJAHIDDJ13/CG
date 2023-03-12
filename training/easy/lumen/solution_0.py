import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())

room = [[0 for _ in range(n)] for _ in range(n)]
orig = []
for i in range(n):
    line = input().split()
    orig.append(line)
    
for i in range(n):
    for j in range(n):
        if orig[i][j] == 'C':
            for u in range(i-l+1, i+l):
                for v in range(j-l+1, j+l):
                    if u>=0 and u<n and v>=0 and v<n:
                        room[u][v] += 1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print('\n'.join([' '.join(map(str,line)) for line in room]), file=sys.stderr)
print(sum([sum([l==0 for l in line]) for line in room]))

