import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
cells = []
for i in range(n):
    operation, arg1, arg2 = input().split()
    cells += [(operation, arg1, arg2)]
cell_vals = []

memoized_vals = [False] * n
def get_cell_val(n):
    def seek_value(x):
        if x[0] != '$':
            val = int(x)
            return val
        else:
            ref = int(x[1:])
            if memoized_vals[ref] == False:
                memoized_vals[ref] = get_cell_val(ref)
            return memoized_vals[ref]

    op, a1, a2 = cells[n]
    a1 = seek_value(a1)
    if op == 'VALUE':
        return a1

    a2 = seek_value(a2)
    if op == 'ADD':
        return a1+a2
    elif op == 'SUB':
        return a1-a2
    elif op == 'MULT':
        return a1*a2

print("\n".join([str(get_cell_val(i)) for i in range(n)]))