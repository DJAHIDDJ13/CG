import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def happy(x):
    seen = []
    while x not in seen and x != 1:
        seen += [x]
        x = sum([int(c)**2 for c in str(x)])
    return x == 1
n = int(input())
for i in range(n):
    x = input()
    print(x, ':)' if happy(x) else ':(')

