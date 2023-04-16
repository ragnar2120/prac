import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class RBFNet():
    def __init__(self, n_hidden, gamma=1.0):
        self.n_hidden = n_hidden
        self.gamma = gamma
        self.hidden_centers = None
        self.hidden_widths = None
        self.output_weights = None
        self.label_binarizer = LabelBinarizer()

    def _calculate_hidden_layer(self, X):
        D = euclidean_distances(X, self.hidden_centers)
        H = np.exp(-self.gamma * D ** 2)
        return H

    def _initialize_centers(self, X):
        kmeans = KMeans(n_clusters=self.n_hidden)
        kmeans.fit(X)
        self.hidden_centers = kmeans.cluster_centers_

    def _initialize_widths(self, X):
        D = euclidean_distances(X, self.hidden_centers)
        self.hidden_widths = np.sqrt(1 / (2 * self.n_hidden) * np.sum(D ** 2))

    def fit(self, X, y):
        self.label_binarizer.fit(y)
        y = self.label_binarizer.transform(y)
        self._initialize_centers(X)
        self._initialize_widths(X)
        H = self._calculate_hidden_layer(X)
        self.output_weights = np.dot(np.linalg.pinv(H), y)

    def predict(self, X):
        H = self._calculate_hidden_layer(X)
        y_pred = np.dot(H, self.output_weights)
        return self.label_binarizer.inverse_transform(y_pred)

# generate data
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=1, n_clusters_per_class=1)

# train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)

# train RBF network
rbf = RBFNet(10)
rbf.fit(X_train, y_train)

# predict on test set
y_pred = rbf.predict(X_test)

# compute accuracy
acc = accuracy_score(y_test, y_pred)

# plot decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = rbf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
plt.title('RBF Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Define colormap for the plot
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])

# Create meshgrid for the plot
h = 0.02  # step size in the mesh
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
X_grid = np.c_[xx.ravel(), yy.ravel()]

# Make predictions on the meshgrid
Z = rbf.predict(X_grid)
Z = Z.reshape(xx.shape)

# Plot the decision boundaries
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot the training data
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('RBF decision boundaries on Iris dataset')
plt.show()
print("Accuracy on test data: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
