import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

numr = 1
denr = int(input())

d = ""
seen = {}
rem = numr % denr
 
while rem != 0 and rem not in seen:
    seen[rem] = len(d)
    rem = rem * 10
 
    q = rem // denr
    d += str(q)

    rem = rem % denr


if rem == 0:
    print(f'0.{d}')
else:
    i = seen[rem]
    print(f'0.{d[:i]}({d[i:]})')