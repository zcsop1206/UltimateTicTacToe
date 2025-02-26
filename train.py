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
            current_player = game.current_player
            agent = agent_x if current_player == 1 else agent_o

            # Determine the legal actions for the current player
            legal_actions = [i+1 for i in range(9) if game.board[i] == 0]
            action = agent.act(state, legal_actions)
            next_state, reward, done = game.step(action)
            
            if current_player == 1:
                total_reward_x += reward
                agent_x.remember(state, action, reward, next_state, done)
            else:
                total_reward_o += reward
                agent_o.remember(state, action, reward, next_state, done)

            state = next_state

        # Print progress every 100 episodes and save models
        if e % 100 == 0:
            print(f"Episode {e}/{episodes}, Total Reward X: {total_reward_x}, Total Reward O: {total_reward_o}")
            agent_x.save_model('agent_x_model.pth')
            agent_o.save_model('agent_o_model.pth')
            time.sleep(1)

if __name__ == "__main__":
    train()
