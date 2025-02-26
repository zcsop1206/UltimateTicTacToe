from agent import QAgent
from game import TicTacToe
import time

def train():
    agent_x = QAgent()  # Agent playing as 'X'
    agent_o = QAgent()  # Agent playing as 'O'
    game = TicTacToe()
    episodes = 10000

    for e in range(episodes):
        state = game.reset()
        done = False
        total_reward_x = 0
        total_reward_o = 0
        current_agent = agent_x  # 'X' starts first

        while not done:
            legal_actions = [i for i in range(9) if state[i] == 0]
            action = current_agent.act(state, legal_actions)
            next_state, reward, done = game.step(action, 1 if current_agent == agent_x else -1)

            if current_agent == agent_x:
                total_reward_x += reward
                agent_x.remember(state, action, reward, next_state, done)
                current_agent = agent_o  # Switch to 'O'
            else:
                total_reward_o += reward
                agent_o.remember(state, action, reward, next_state, done)
                current_agent = agent_x  # Switch to 'X'

            state = next_state

        # Print rewards every 100 episodes
        if e % 100 == 0:
            print(f"Episode {e}/{episodes}, Total Reward X: {total_reward_x}, Total Reward O: {total_reward_o}")
            time.sleep(1)  # Reduced sleep time for faster training

if __name__ == "__main__":
    train()
