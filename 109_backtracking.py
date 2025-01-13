def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nqueens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_nqueens(board, 0, n):
        return board
    return None

n = 5
solution = n_queens(n)
for row in solution:
    print(row)





























# Explanation: The backtracking approach tries to place a queen in each column
# and checks for conflicts. If placing a queen leads to a solution, the board 
# is returned. If not, it backtracks.