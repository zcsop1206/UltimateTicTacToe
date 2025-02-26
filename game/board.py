def print_board(board):
    # Map the values in the board to 'X', 'O', or empty space
    board_display = ['X' if x == 1 else 'O' if x == -1 else ' ' for x in board]
    
    for i in range(0, 9, 3):
        # Print the row, joined by ' | ' for better formatting
        print(" | ".join(board_display[i:i+3]))
        
        if i < 6:
            print("-" * 10)  # Print a separator between rows
