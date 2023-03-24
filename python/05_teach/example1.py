import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create some example data
x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
y = np.array([2, 3.9, 6.1, 8, 10.1])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
data = model.fit(x,y)

print(data.score(x,y))

# Predict the values for some new data
x_new = np.array([6, 7]).reshape((-1, 1))
y_new = model.predict(x_new)

print(y_new)

print(model.predict(x))

# Plot the data and the linear regression line
plt.scatter(x, y)
plt.plot(x, model.predict(x), color='green')

# Plot the predicted values for the new data points
plt.scatter(x_new, y_new, color='red')

# Add labels and a title to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Example')

# Show the plot
plt.show()

