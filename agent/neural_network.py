import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, output_size, hidden_size=64, learning_rate=0.01):
        # Initialize neural network parameters
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Weights initialization: Xavier initialization
        self.W1 = np.random.randn(self.input_size, self.hidden_size) / np.sqrt(self.input_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size) / np.sqrt(self.hidden_size)
        self.b2 = np.zeros((1, self.output_size))

    def forward(self, X):
        # Forward pass through the network
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = self.tanh(self.Z1)  # Activation function (tanh)
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = self.Z2  # Output layer (no activation for Q-values)
        return self.A2

    def backward(self, X, y):
        # Backpropagation: Compute gradients
        m = X.shape[0]
        
        # Compute gradients for output layer
        dZ2 = self.A2 - y
        dW2 = np.dot(self.A1.T, dZ2) / m
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m
        
        # Compute gradients for hidden layer
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * (1 - np.power(self.A1, 2))  # Derivative of tanh
        dW1 = np.dot(X.T, dZ1) / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m
        
        # Update weights using gradient descent
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2

    def train(self, X, y):
        # Train the network using forward and backward propagation
        self.forward(X)
        self.backward(X, y)

    def tanh(self, x):
        return np.tanh(x)

    def tanh_derivative(self, x):
        return 1.0 - np.tanh(x)**2
