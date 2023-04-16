import numpy as np
import matplotlib.pyplot as plt

def find_bmu(som, x):
    distances = np.linalg.norm(som - x, axis=2)
    return np.unravel_index(np.argmin(distances), som.shape[:2])

def update_weights(som, train_example, learn_rate, radius, bmu_coords):
    row_indices, col_indices = np.indices(som.shape[:2])
    dist_to_bmu = np.linalg.norm(np.dstack([row_indices, col_indices]) - bmu_coords, axis=2)
    neighborhood = np.exp(-dist_to_bmu**2 / (2*radius**2))
    som += learn_rate * neighborhood[:,:,np.newaxis] * (train_example - som)

def train_som(som, train_data, learn_rate=0.1, radius=1, lr_decay=0.1, radius_decay=0.1, epochs=10):
    learn_rate_0 = learn_rate
    radius_0 = radius
    for epoch in range(epochs):
        np.random.shuffle(train_data)
        for train_example in train_data:
            bmu_coords = find_bmu(som, train_example)
            update_weights(som, train_example, learn_rate, radius, bmu_coords)
        learn_rate = learn_rate_0 * np.exp(-epoch * lr_decay)
        radius = radius_0 * np.exp(-epoch * radius_decay)
    return som

m = 10
n = 10
n_x = 3000
rand = np.random.RandomState(0)
train_data = rand.randint(0, 255, (n_x, 3))
som = rand.randint(0, 255, (m, n, 3)).astype(float)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 3.5), subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(train_data.reshape(50, 60, 3))
ax[0].title.set_text('Training Data')
ax[1].imshow(som.astype(int))
ax[1].title.set_text('Randomly Initialized SOM Grid')

fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(40, 40), subplot_kw=dict(xticks=[], yticks=[]))
total_epochs = 0

for epochs, ax_row in zip([10, 20, 50, 100], ax):
    for epoch, ax_subplot in zip(range(epochs), ax_row):
        sample = rand.randint(0, 255, (1, 3))
        bmu_coords = find_bmu(som, sample)
        ax_subplot.imshow(sample.reshape(1, 1, 3))
        ax_subplot.title.set_text('BMU (Epochs = {})'.format(total_epochs))
        ax_subplot.set_xlabel('({},{})'.format(bmu_coords[0], bmu_coords[1]))
    total_epochs += epochs


plt.show()
