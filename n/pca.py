import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

# Define PCA function
def pca(X, k):
    # Calculate covariance matrix
    cov_matrix = np.cov(X.T)
    
    # Calculate eigenvalues and eigenvectors of covariance matrix
    eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
    
    # Sort eigenvalues in descending order and keep only k eigenvectors with highest eigenvalues
    idx = np.argsort(eigen_values)[::-1][:k]
    eigen_vectors = eigen_vectors[:, idx]
    
    # Project data onto k-dimensional subspace
    X_reduced = np.dot(X, eigen_vectors)
    
    return X_reduced

# Load iris dataset
iris = load_iris()
X = iris.data

# Apply PCA with k=2
X_reduced = pca(X, 2)

# Create a Pandas DataFrame of reduced dataset
principal_df = pd.DataFrame(X_reduced, columns=['PC1', 'PC2'])

# Concatenate it with target variable to create a complete dataset
principal_df = pd.concat([principal_df, pd.DataFrame(iris.target)], axis=1)
principal_df.columns = ['PC1', 'PC2', 'Target']

# Plot the 2D scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(principal_df[principal_df.Target==0].PC1, principal_df[principal_df.Target==0].PC2, color='r', label=iris.target_names[0])
plt.scatter(principal_df[principal_df.Target==1].PC1, principal_df[principal_df.Target==1].PC2, color='g', label=iris.target_names[1])
plt.scatter(principal_df[principal_df.Target==2].PC1, principal_df[principal_df.Target==2].PC2, color='b', label=iris.target_names[2])
plt.legend()
plt.title('Iris dataset after PCA')
plt.xlabel('PC1')
plt.ylabel('PC2')

# Plot the 3D scatter plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

xs = X[:, 0]
ys = X[:, 1]
zs = X[:, 2]

ax.scatter(xs, ys, zs, s=50, alpha=0.6, edgecolors='b')
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
ax.set_zlabel('Sepal Length')
ax.set_title('Iris dataset in 3D')

plt.show()
