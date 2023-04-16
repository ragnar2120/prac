# From sctrach XOR using MLP

import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# XOR gate inputs and outputs
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights randomly with mean 0
weights1 = 2 * np.random.random((2, 2)) - 1
weights2 = 2 * np.random.random((2, 1)) - 1
bias1 = 2 * np.random.random((1, 2)) - 1
bias2 = 2 * np.random.random((1, 1)) - 1

# Train the network for 10,000 iterations
for i in range(100000):
    # Pass the inputs forward through the network
    layer1 = sigmoid(np.dot(X, weights1) + bias1)
    layer2 = sigmoid(np.dot(layer1, weights2) + bias2)

    # Calculate the error
    error = y - layer2

    # Backpropagate the error
    d_weights2 = np.dot(layer1.T, error * sigmoid_derivative(layer2))
    d_bias2 = np.sum(error * sigmoid_derivative(layer2), axis=0, keepdims=True)
    d_weights1 = np.dot(X.T, np.dot(error * sigmoid_derivative(layer2), weights2.T) * sigmoid_derivative(layer1))
    d_bias1 = np.sum(np.dot(error * sigmoid_derivative(layer2), weights2.T) * sigmoid_derivative(layer1), axis=0)

    # Update the weights
    weights1 += d_weights1
    weights2 += d_weights2
    bias1 += d_bias1
    bias2 += d_bias2

# Plot the decision surface
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2), np.arange(y_min, y_max, 0.2))
Z = np.array([xx.ravel(), yy.ravel()]).T
layer1 = sigmoid(np.dot(Z, weights1) + bias1)
layer2 = sigmoid(np.dot(layer1, weights2) + bias2)
Z = np.round(layer2).reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), edgecolors='k', cmap=plt.cm.Spectral)
plt.show()
