import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
f = []
b = []
rel = [0, 0]
for i in range(n):
    line = input()
    try:
        rel = [i,int(line)]
    except:pass
    if 'Fizz' in line:
        f+= [i]
    if 'Buzz' in line:
        b += [i]
        
shift = rel[1] - rel[0]
diff = lambda x:x[1]-x[0] if len(x)>1 else x[0]+shift
print(diff(f), diff(b))