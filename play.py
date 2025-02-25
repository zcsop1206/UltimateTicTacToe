from agent.q_agent import QAgent
from game.tictactoe import TicTacToe
import time

def train():
    agent = QAgent()
    game = TicTacToe()
    episodes = 10000

    for e in range(episodes):
        state = game.reset()
        done = False
        total_reward = 0

        while not done:
            legal_actions = [i for i in range(9) if state[i] == 0]
            action = agent.act(state, legal_actions)
            next_state, reward, done = game.step(action, 1)
            total_reward += reward
            agent.remember(state, action, reward, next_state, done)
            state = next_state

        # Print Q-table every 100 episodes and wait for 10 seconds
        if e % 100 == 0:
            print(f"Episode {e}/{episodes}, Total Reward: {total_reward}")
            time.sleep(10)

if __name__ == "__main__":
    train()
