import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/bingo.csv')

# print(df.info)

x = df['X'].values.reshape(-1, 1)
y = df['Y']

dataIn = int(input("Enter : "))

# print(x)
# print(y)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
data = model.fit(x,y) # error

# Check Score
# print(data.score(x,y))


y_new = model.predict(x)

# print(y_new)


# Plot the data and the linear regression line
plt.scatter(x, y)
plt.plot(x, model.predict(x), color='green')


# Prediction

non = np.array([dataIn]).reshape((-1, 1))

result = model.predict(non)

print(result)

# Plot the predicted values for the new data points
plt.scatter(non, result, color='red')

# Add labels and a title to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Example')

# Show the plot
plt.show()