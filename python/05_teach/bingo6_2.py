import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('data/SATandGPA.csv')

# print(df.head())
x = df['GPA']
x1 = df['GPA'].values.reshape(-1,1)
y = df['SAT']
y1 = df['SAT'].values.reshape(-1,1)



pl = PolynomialFeatures(degree=33)
x_pl = pl.fit_transform(x1)
y_pl = pl.fit_transform(y1)

model = LinearRegression()
model.fit(x_pl,y)

model2 = LinearRegression()
model2.fit(y_pl,x)



print("\n ===================================== \n")



# print(x_new)
# Predict with the model using the transformed input value
y_predict = model.predict(x_pl)


# Plot the original scatter plot, regression line, and predicted value for the new input
plt.scatter(x1,y,color='blue')
plt.plot(x1,y_predict,alpha = 0.4,
         color ='red', linestyle ='dashed',
         linewidth = 2, marker ='D',
         markersize = 5, markerfacecolor ='blue',
         markeredgecolor ='blue')

plt.show()

print("\n ===================================== \n")
print("ok")


