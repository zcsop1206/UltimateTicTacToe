from agent import QAgent
from game import TicTacToe
from game import print_board

def play_against_agent():
    agent = QAgent()
    game = TicTacToe()

    # Let the human player choose their marker
    human_marker = ''
    while human_marker not in ['X', 'O']:
        human_marker = input("Choose your marker (X/O): ").upper()

    agent_marker = 'O' if human_marker == 'X' else 'X'
    human_player = 1 if human_marker == 'X' else -1
    agent_player = -human_player

    print(f"You are '{human_marker}' and the agent is '{agent_marker}'.")
    print("Board positions (0-8):")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    print("\n")

    while True:
        state = game.reset()
        done = False
        while not done:
            if game.current_player == human_player:
                # Human's turn
                legal_actions = [i for i in range(9) if state[i] == 0]
                print_board(game.board)
                print("Your turn. Choose position (0-8):")
                action = -1
                while action not in legal_actions:
                    try:
                        action = int(input())
                        if action not in legal_actions:
                            print("Invalid move. Choose again.")
                    except ValueError:
                        print("Invalid input. Enter a number between 0 and 8.")
                next_state, reward, done = game.step(action, human_player)
            else:
                # Agent's turn
                legal_actions = [i for i in range(9) if state[i] == 0]
                action = agent.act(state, legal_actions)
                next_state, reward, done = game.step(action, agent_player)
                print(f"Agent ('{agent_marker}') chooses position {action}.")

            state = next_state

            if done:
                print_board(game.board)
                if reward == 1:
                    if game.current_player == -human_player:
                        print("You win!")
                    else:
                        print("Agent wins!")
                else:
                    print("It's a draw!")
                break

if __name__ == "__main__":
    play_against_agent()
