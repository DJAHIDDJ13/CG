import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, m, c = [int(i) for i in input().split()]
app = [False] * n
caps = [0] * n
for i, v in enumerate(input().split()):
    nx = int(v)
    caps[i] = nx
blown = False
max_cons = 0
for i in input().split():
    mx = int(i)
    app[mx-1] = not app[mx-1]
    cur_cons = sum([a*b for a,b in zip(app, caps)])
    max_cons = max(max_cons, cur_cons)

print('Fuse was blown.' if max_cons > c else 'Fuse was not blown.')
if max_cons <= c:
    print(f"Maximal consumed current was {max_cons} A.")
