def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join([str(board[j]) if board[j] != 0 else " " for j in range(i, i+3)]))
        if i < 6:
            print("-" * 5)
