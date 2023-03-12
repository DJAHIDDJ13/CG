from itertools import combinations
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = int(input())
n = int(input())
bars = []
for i in input().split():
    bar = int(i)
    bars += [bar]
combs = []

min_comb = []
min_val = 10000000
for l in range(1,2**n):
    bitmap = bin(l)[2:].zfill(n)[::-1]
    comb = []
    s = 0
    for i, bit in enumerate(bitmap):
        if bit == '1':
            s+=bars[i]
            comb += [bars[i]]
    if s <= m:
        a = abs(m - s)
        if a <= min_val:
            min_comb = comb
            min_val = a
print(' '.join(map(str,min_comb)))