from agent import QAgent
from game import TicTacToe, print_board

def play_against_agent():
    # Let the human player choose their marker
    human_marker = ''
    while human_marker not in ['X', 'O']:
        human_marker = input("Choose your marker (X/O): ").upper()

    agent_marker = 'O' if human_marker == 'X' else 'X'
    human_player = 1 if human_marker == 'X' else -1
    agent_player = -human_player

    # Load the appropriate trained agent
    agent = QAgent()
    model_path = 'agent_x_model.pth' if agent_marker == 'X' else 'agent_o_model.pth'
    agent.load_model(model_path)

    game = TicTacToe()

    print(f"You are '{human_marker}' and the agent is '{agent_marker}'.")
    print("Board positions are numbered from 1 to 9 (for a 3x3 board).")
    print("\n")

    while True:
        state = game.reset()
        done = False
        while not done:
            if game.current_player == human_player:
                # Human's turn
                legal_actions = legal_actions = [i+1 for i in range(9) if game.board[i] == 0]
                print_board(game.board)
                print("Your turn. Choose position (1-9):")
                action = -1
                while action not in legal_actions:
                    try:
                        action = int(input())-1
                        if action not in legal_actions:
                            print("Invalid move. Choose again.")
                    except ValueError:
                        print("Invalid input. Enter a number between 1 and 9.")
                next_state, reward, done = game.step(action)
            else:
                # Agent's turn
                legal_actions = legal_actions = [i+1 for i in range(9) if game.board[i] == 0]
                action = agent.act(state, legal_actions)
                next_state, reward, done = game.step(action)
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
