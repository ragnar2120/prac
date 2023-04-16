# Odd and Even classification
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0, 0, 0, 0],
[0, 0, 1, 1],
[0, 1, 0, 0],
[0, 1, 1, 1],
[1, 0, 0, 0],
[1, 0, 1, 1],
[1, 1, 0, 0],
[1, 1, 1, 1]
])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = data[:, :3]
y = data[:, 3:]

np.random.seed(1)
weights_0_1 = 2 * np.random.random((3, 4)) - 1
weights_1_2 = 2 * np.random.random((4, 1)) - 1

for i in range(2000):
    layer_0 = X
    layer_1 = sigmoid(np.dot(layer_0, weights_0_1))
    layer_2 = sigmoid(np.dot(layer_1, weights_1_2))

    layer_2_error = y - layer_2
    layer_2_delta = layer_2_error * sigmoid_derivative(layer_2)

    layer_1_error = layer_2_delta.dot(weights_1_2.T)
    layer_1_delta = layer_1_error * sigmoid_derivative(layer_1)

    weights_1_2 += layer_1.T.dot(layer_2_delta)
    weights_0_1 += layer_0.T.dot(layer_1_delta)

predictions = np.round(layer_2)
print("Predictions: \n", predictions)
print("Expected: \n", y)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(y, 'b', label='Expected Output')
ax1.set_xlabel('Sample Number')
ax1.set_ylabel('Output Value')
ax1.set_title('Expected Output')
ax1.legend(loc='best')

ax2.plot(predictions, 'r', label='Predicted Output')
ax2.set_xlabel('Sample Number')
ax2.set_ylabel('Output Value')
ax2.set_title('Predicted Output')
ax2.legend(loc='best')

plt.tight_layout()
plt.show()
