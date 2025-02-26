from agent import QAgent
from game import TicTacToe
import time

def train():
    agent_x = QAgent()
    agent_o = QAgent()
    game = TicTacToe()
    episodes = 10000

    for e in range(episodes):
        state = game.reset()
        done = False
        total_reward_x = 0
        total_reward_o = 0

        while not done:
            if game.current_player == 1:
                # X's turn
                legal_actions = legal_actions = [i for i in range(9) if game.board[i] == 0]
                action = agent_x.act(state, legal_actions)
                next_state, reward, done = game.step(action)
                total_reward_x += reward
                agent_x.remember(state, action, reward, next_state, done)
            else:
                # O's turn
                legal_actions = legal_actions = [i for i in range(9) if game.board[i] == 0]
                action = agent_o.act(state, legal_actions)
                next_state, reward, done = game.step(action)
                total_reward_o += reward
                agent_o.remember(state, action, reward, next_state, done)

            state = next_state

        # Print progress every 100 episodes
        if e % 100 == 0:
            print(f"Episode {e}/{episodes}, Total Reward X: {total_reward_x}, Total Reward O: {total_reward_o}")
            time.sleep(1)

    # Save trained models
    agent_x.save_model('agent_x_model.pth')
    agent_o.save_model('agent_o_model.pth')

if __name__ == "__main__":
    train()
