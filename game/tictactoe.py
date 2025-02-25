class TicTacToe:
    def __init__(self):
        self.board = [0] * 9  # Empty board (0 means empty)
        self.current_player = 1  # Player 1 starts

    def reset(self):
        self.board = [0] * 9
        self.current_player = 1
        return self.board

    def step(self, action, player):
        if self.board[action] == 0:
            self.board[action] = player
            reward = self.check_win(player)
            done = reward != 0 or all(x != 0 for x in self.board)  # Game over
            self.current_player = -self.current_player
            return self.board, reward, done
        return self.board, 0, False

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return 1
        return 0
