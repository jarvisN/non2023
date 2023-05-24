import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LogisticRegression

# Generate random data for demonstration
np.random.seed(0)
n_samples = 100

# Generate random input features
X1 = np.random.randn(n_samples, 1)
X2 = np.random.randn(n_samples, 1)
X = np.hstack((X1, X2))

# Generate random target labels
y = np.random.randint(0, 2, size=(n_samples,))

# Create and fit the logistic regression model
logreg = LogisticRegression()
logreg.fit(X, y)

# Generate a meshgrid of points to evaluate the model
x1_min, x1_max = X1.min() - 1, X1.max() + 1
x2_min, x2_max = X2.min() - 1, X2.max() + 1
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max, 100), np.linspace(x2_min, x2_max, 100))
grid_points = np.c_[xx1.ravel(), xx2.ravel()]

# Make predictions on the meshgrid points
y_pred = logreg.predict(grid_points)
y_pred = y_pred.reshape(xx1.shape)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points and decision surface
ax.scatter(X1[y == 0], X2[y == 0], 0, color='blue', label='Class 0')
ax.scatter(X1[y == 1], X2[y == 1], 0, color='red', label='Class 1')
ax.plot_surface(xx1, xx2, y_pred, alpha=0.5, cmap='viridis')

# Set labels and legend
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Predicted Probability')
ax.set_title('Multiple Logistic Regression')
ax.legend()

# Show the 3D plot
plt.show()
