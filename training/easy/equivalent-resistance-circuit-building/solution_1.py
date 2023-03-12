import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
r_map = {}
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    r_map[name] = r
circuit = input()

def rec_circuit(c, cont_idx, r_map):
    operands = []
    if c[cont_idx] == '(':
        i = cont_idx+1
        while c[i] != ')':
            val, idx = rec_circuit(c, i, r_map)
            operands += [val]
            i=idx
        
        return sum(operands), i + 1
    elif c[cont_idx] == '[':
        i = cont_idx+1
        while c[i] != ']':
            val, idx = rec_circuit(c, i, r_map)
            operands += [1.0 / val]
            i=idx
        return 1.0 / sum(operands), i + 1
    else:
        return r_map[c[cont_idx]], cont_idx + 1

print("%.1f"%rec_circuit(circuit.split(), 0, r_map)[0])