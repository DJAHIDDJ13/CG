import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

exp = "".join([i if i in "()[]{}" else '' for i in input()])
i = 0
while i<len(exp)-2:
    if exp[i:i+2] in ['()', '[]', '{}']:
        exp = exp[:i]+exp[i+2:]
        i=-1
    i+=1
print("true" if exp in  ['()', '[]', '{}'] else "false")
