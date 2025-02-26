import numpy as np
from neural_network import NeuralNetwork

class QAgent:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=0.9, input_size=9, output_size=9, model=None):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.model = model if model else NeuralNetwork(input_size, output_size)

    def act(self, state, legal_actions):
        # Epsilon-greedy strategy
        if np.random.random() < self.epsilon:
            return np.random.choice(legal_actions)
        else:
            q_values = self.model.forward(np.array([state]))
            q_values = q_values[0]  # Flatten the output
            q_values = [q_values[i] if i in legal_actions else -np.inf for i in range(len(q_values))]
            return np.argmax(q_values)

    def remember(self, state, action, reward, next_state, done):
        # Convert state and next_state to numpy arrays for training
        state = np.array([state])
        next_state = np.array([next_state])
        # Predict Q-values for current state and next state
        q_values = self.model.forward(state)
        next_q_values = self.model.forward(next_state)

        # Target Q-value
        target = q_values[0, action] + self.alpha * (reward + self.gamma * np.max(next_q_values) * (1 - done) - q_values[0, action])
        
        # Update the model with the new Q-value
        target_q_values = np.copy(q_values)
        target_q_values[0, action] = target
        self.model.train(state, target_q_values)

    def replay(self):
        # Placeholder for experience replay if needed
        pass

    def load_model(self, model_path):
        # Load the model parameters (weights) from numpy files
        self.model.W1 = np.load(model_path + '_W1.npy')
        self.model.b1 = np.load(model_path + '_b1.npy')
        self.model.W2 = np.load(model_path + '_W2.npy')
        self.model.b2 = np.load(model_path + '_b2.npy')

    def save_model(self, model_path):
        # Save the model parameters (weights) to numpy files
        np.save(model_path + '_W1.npy', self.model.W1)
        np.save(model_path + '_b1.npy', self.model.b1)
        np.save(model_path + '_W2.npy', self.model.W2)
        np.save(model_path + '_b2.npy', self.model.b2)
