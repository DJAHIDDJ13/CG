
from pprint import pprint
rook_position = input()
nb_pieces = int(input())
board = [[0 for _ in range(8)] for _ in range(8)]

pos2coord = lambda p: ("abcdefgh".index(p[0]), int(p[1])-1)
coord2pos = lambda x,y: f'{"abcdefgh"[x]}{y+1}'
for i in range(nb_pieces):
    inputs = input().split()
    colour = int(inputs[0])
    one_piece = inputs[1]
    x, y = pos2coord(one_piece)

    board[y][x] = 1-colour*2

x, y = pos2coord(rook_position)
moves = []
for i in range(x+1, 8):
    if board[y][i] == 1:break
    if board[y][i] == -1:
        moves += [f"R{rook_position}x{coord2pos(i, y)}"]
        break
    moves += [f"R{rook_position}-{coord2pos(i, y)}"]
for i in range(x-1, -1, -1):
    if board[y][i] == 1:break
    if board[y][i] == -1:
        moves += [f"R{rook_position}x{coord2pos(i, y)}"]
        break
    moves += [f"R{rook_position}-{coord2pos(i, y)}"]
for j in range(y-1, -1, -1):
    if board[j][x] == 1:break
    if board[j][x] == -1:
        moves += [f"R{rook_position}x{coord2pos(x, j)}"]
        break
    moves += [f"R{rook_position}-{coord2pos(x, j)}"]
for j in range(y+1, 8):
    if board[j][x] == 1:break
    if board[j][x] == -1:
        moves += [f"R{rook_position}x{coord2pos(x, j)}"]
        break
    moves += [f"R{rook_position}-{coord2pos(x, j)}"]

moves = sorted(moves)
print(*moves, sep='\n')
