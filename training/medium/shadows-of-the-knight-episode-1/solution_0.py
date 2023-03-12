import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
box=[[x0,y0],[]]
init = input()
if 'R' in init:
    box[1].append(w-1)
elif 'L' in init:
    box[1].append(0)
else:
    box[1].append(x0)
    
if 'U' in init:
    box[1].append(0)
elif 'D' in init:
    box[1].append(h-1)
else:
    box[1].append(y0)
x0 = (box[0][0]+box[1][0])//2
y0 = (box[0][1]+box[1][1])//2
print(init, file=sys.stderr)
print(box, file=sys.stderr)
print(x0,y0,file=sys.stderr)
print(x0,y0)
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    MAXX = 0 if box[0][0]>box[1][0] else 1    
    MAXY = 0 if box[0][1]>box[1][1] else 1
    if 'U' in bomb_dir:
        box[MAXY][1]=y0
    elif 'D' in bomb_dir:
        box[1-MAXY][1]=y0
    if 'L' in bomb_dir:
        box[MAXX][0]=x0
    elif 'R' in bomb_dir:
        box[1-MAXX][0]=x0
        
    
    if box[0][0]!=box[1][0]:
        if abs(box[0][0]-box[1][0])==1:
            if 'R' in bomb_dir:
                x0 = box[MAXX][0]
            if 'L' in bomb_dir:
                x0 = box[1-MAXX][0]
        else:
            x0 = (box[0][0]+box[1][0])//2
    if box[0][1]!=box[1][1]:
        if abs(box[0][1]-box[1][1])==1:
            if 'U' in bomb_dir:
                y0 = box[1-MAXY][1]
            if 'D' in bomb_dir:
                y0 = box[MAXY][1]
        else:
            y0 = (box[0][1]+box[1][1])//2
    # Write an action using print
    print(bomb_dir, file=sys.stderr)
    print(box, file=sys.stderr)
    print(x0,y0,file=sys.stderr)
    print(x0,y0)

