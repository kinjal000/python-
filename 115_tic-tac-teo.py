def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

board = [[" "]*3 for _ in range(3)]
turn = "X"

for i in range(9):
    print_board(board)
    row, col = map(int, input(f"Player {turn}, enter row and column (0-2): ").split())
    if board[row][col] == " ":
        board[row][col] = turn
        if check_win(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        turn = "O" if turn == "X" else "X"
    else:
        print("Cell already occupied, try again.")
else:
    print("It's a draw!")
























# Explanation:

# Two players take turns to place "X" and "O" on the grid.
# The game checks for a win after each move