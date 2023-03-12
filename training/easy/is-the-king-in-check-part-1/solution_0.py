import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
chess = []
pos = {}
for i in range(8):
    chess_row = input().split()
    for j,c in enumerate(chess_row):
        if c != '_':
            pos[c] = (i,j)
    chess += [chess_row]

checked = False
kingx, kingy = pos['K']

if 'N' in pos:
    for a,b in [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]:
        a, b = a+pos['N'][0], b+pos['N'][1]
        if a == kingx and b == kingy:
            checked = True
elif 'R' in pos:
    if pos['R'][0] == kingx or pos['R'][1] == kingy:
        checked = True
elif 'B' in pos:
    a,b = abs(pos['B'][0]-kingx), abs(pos['B'][1]-kingy)
    if a == b:
        checked = True
elif 'Q' in pos:
    if pos['Q'][0] == kingx or pos['Q'][1] == kingy:
        checked = True
    a,b = abs(pos['Q'][0]-kingx), abs(pos['Q'][1]-kingy)
    if a == b:
        checked = True

print(['No Check', 'Check'][checked])