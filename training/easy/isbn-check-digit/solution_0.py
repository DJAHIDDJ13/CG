import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
codes = []
digitmap = ''.join(map(str,range(10))) + 'X'
for i in range(n):
    isbn = input()
    if len(isbn) not in [10, 13]:
        codes += [isbn]
        continue
    if any(x not in digitmap[:-1] for x in isbn[:-1]):
        codes += [isbn]
        continue
    if isbn[-1] not in digitmap:
        codes += [isbn]
        continue

    if len(isbn) == 10:
        mod, checklist = 11, range(10, 1, -1)
    else:
        mod, checklist = 10, [1, 3] * 6
    
    check = sum([int(v) * i for v, i in zip(isbn[:-1], checklist)])
    check = (mod - check % mod) % mod 
    check = digitmap[check]
    
    if check != isbn[-1]:
        codes += [isbn]
print(f'{len(codes)} invalid:')
print(*codes, sep='\n')