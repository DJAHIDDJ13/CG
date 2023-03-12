import sys

# read the input
w, h = map(int, input().split())
m = []
DIRECTIONS = {'>': (1, 0),
              'v': (0, 1),
              '<': (-1, 0),
              '^': (0, -1)}

direction = None
sx, sy = None, None
for i in range(h):
    row = input()
    line = []
    for j, c in enumerate(row):
        if c in DIRECTIONS:
            direction = c
            sx, sy = j, i
        line.append('#' if c == '#' else 0)
    m.append(line)

if direction is None:
    exit(1)
side = input()
left_of = {'v': '<', '>': 'v', '<': '^', '^': '>'}
right_of = {'v': '>', '>': '^', '<': 'v', '^': '<'}
dir_of = right_of if side == 'L' else left_of

x, y = sx, sy
while True:
    for d in [dir_of[direction], 
              direction, 
              dir_of[dir_of[dir_of[direction]]], 
              dir_of[dir_of[direction]]]:
        dx, dy = DIRECTIONS[d]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < w and 0 <= ny < h and m[ny][nx] != '#':
            x, y = nx, ny
            m[ny][nx] += 1
            direction = d
            break

    if (x, y) == (sx, sy):
        break

for line in m:
    print(*line, sep="")