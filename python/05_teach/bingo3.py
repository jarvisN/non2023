import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


DB = pd.read_csv('data/bingo.csv')



x = DB['X'].values.reshape((-1, 1))
y = DB['Y']

lr = LinearRegression()

data = lr.fit(x,y)


new_x = np.array([10]).reshape((-1, 1))
print(new_x)

# print(x)
# print(y)




# # Create a linear regression model
# lr = LinearRegression()



# # Fit the model to the data
# lr.fit(x,y)




# x_new = np.array(x).reshape((-1, 1))
# y_new = lr.predict(x_new)

# plt.scatter(x, y)
# plt.plot(x, model.predict(x), color='green')