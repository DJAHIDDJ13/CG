import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = input()
def find_clumps(m, b):
    cur_mod = int(m[0]) % b
    clumps = [[m[0]]]
    for i in range(1, len(m)):
        if cur_mod != int(m[i])%b:
            clumps += [[m[i]]]
        else:
            clumps[-1].append(m[i])
        cur_mod = int(m[i])%b

    return clumps

all_clumps = [len(find_clumps(n, b)) for b in range(2, 10)]
pv = all_clumps[0]
behavior = 'Normal'
b = 3
for v in all_clumps[1:]:
    if v < pv:
        behavior = b
        break
    b += 1
    pv = v
print(behavior)