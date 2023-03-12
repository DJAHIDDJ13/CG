import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def inside(point, vs):
    x,y = point
    
    inside = False
    j=len(vs)-1
    for i in range(len(vs)):
        xi, yi = vs[i]
        xj, yj = vs[j]
        
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if (intersect): 
            inside = not inside
        j = i
    
    return inside


n = int(input())
poly = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    poly += [(x,y)]
m = int(input())
for i in range(m):
    x, y = [int(j) for j in input().split()]
    print('hit' if inside((x,y), poly) else 'miss')

