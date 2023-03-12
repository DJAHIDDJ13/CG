import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
from pprint import pprint
def check_win(board):
    rows = [''.join([board[i][j] for j in range(3)]) for i in range(3)]
    cols = [''.join([board[j][i] for j in range(3)]) for i in range(3)]
    diag = [''.join([board[i][i] for i in range(3)]), ''.join([board[2-i][i] for i in range(3)])]
    check_line = lambda x:x=='OOO'
    return any(map(check_line, rows)) or any(map(check_line, cols)) or any(map(check_line, diag))

def get_children(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                new_board = [board[k].copy() for k in range(3)]
                new_board[i][j] = 'O'
                yield new_board

board = []
for i in range(3):
    line = input()
    board += [list(line)]

winning_board = []
for new_board in get_children(board):
    if check_win(new_board):
        winning_board = new_board

print('\n'.join([''.join(l) for l in winning_board]) if winning_board else 'false')