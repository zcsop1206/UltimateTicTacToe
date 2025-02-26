class TicTacToe:
    def __init__(self):
        self.board = [0] * 9  # Empty board (0 means empty)
        self.current_player = 1  # Player 1 starts

    def reset(self):
        self.board = [0] * 9
        self.current_player = 1  # Always start with Player 1 (X)
        return self.board

    def step(self, action):
        if self.board[action] == 0:
            self.board[action] = self.current_player  # Mark the board with the current player's move
            reward = self.check_win(self.current_player)  # Check if the current player wins
            done = reward != 0 or all(x != 0 for x in self.board)  # Game over if someone wins or board is full
            self.current_player = -self.current_player  # Switch player after the move
            return self.board, reward, done
        return self.board, 0, False  # Invalid move, no reward, game continues

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return 1  # Return 1 if the current player wins
        return 0  # No winner yet
