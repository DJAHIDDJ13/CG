import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
def print_tri(m, padding=0, rep=0, start_dot=False):
    for i in range(n):
        v = 2 * i + 1
        w = (n-i-1)
        spaces = w * ' '
        stars = v * '*'
        s = spaces + stars + (' '+spaces + spaces + stars ) * rep
        if start_dot and i==0:
            print('.', (padding-1)*" ", s, sep="")
        else:
            print(padding * " ", s, sep="")

print_tri(n, padding=n, start_dot=True)
print_tri(n, rep=1)

