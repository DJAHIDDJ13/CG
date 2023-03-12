def check_value(board, row, col, number):
    for i in range(9):
        if board[row][i] == number or board[i][col] == number:
            return False

    lo_row = 3 * (row // 3)
    lo_col = 3 * (col // 3)

    for i in range(lo_row, lo_row+3):
        for j in range(lo_col, lo_col+3):
            if board[i][j] == number:
                return False

    return True
    
def backtracking(board, missing_i):
    i = 0
    while i < len(missing_i):
        row = missing_i[i][0]
        column = missing_i[i][1]
        number = board[row][column] + 1
        found = False

        while not found and number <= 9:
            if check_value(board, row, column, number):
                found = True
                board[row][column] = number
                i += 1
            else:
                number += 1

        if not found:
            board[row][column] = 0
            i -= 1
  
    return board

missing_i = []
board = []
for i in range(9):
    line = list(input())
    board += [[]]
    for j,c in enumerate(line):
        if c == '0':
            missing_i += [[i, j]]
        board[-1].append(int(c))

solution = backtracking(board, missing_i)
for line in solution:
    for c in line:
        print(end=str(c))
    print()