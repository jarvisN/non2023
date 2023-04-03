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

# print(x)

# print("\n ===================================== \n")

# print(y)

# plt.scatter(x,y)
# plt.show()

# print("\n ===================================== \n")




pl = PolynomialFeatures(degree=33)
x_pl = pl.fit_transform(x1)
y_pl = pl.fit_transform(y1)

model = LinearRegression()
model.fit(x_pl,y)

model2 = LinearRegression()
model2.fit(y_pl,x)

# score = model.score(x_pl, y)
# print(f'R-squared score: {score}')

# y_predict = model.predict(x_pl)
# plt.scatter(x1,y,color='blue')
# plt.plot(x1,y_predict,color='red')
# plt.show()


print("\n ===================================== \n")

# for i in range(500):
#     pl = PolynomialFeatures(degree=i)
#     x_pl = pl.fit_transform(x1)

#     model = LinearRegression()
#     model.fit(x_pl,y)

#     score = model.score(x_pl, y)*100
#     print(f'R-squared score: {score}')


#     if score > 48:
        
#         print(f'Degree : {i} , Score : {score}')
        
#         y_predict = model.predict(x_pl)
#         plt.scatter(x1,y,color='blue')
#         plt.plot(x1,y_predict,color='red')
#         plt.show()



print("\n ===================================== \n")





# print(x_new)
# Predict with the model using the transformed input value
y_predict = model.predict(x_pl)
x_predict = model2.predict(y_pl)

non = 1800


# # Transform the input value into a polynomial feature array of degree 33
non_new = pl.transform([[non]])

lnwnon = model2.predict(non_new)

print(lnwnon)



# Plot the original scatter plot, regression line, and predicted value for the new input
plt.scatter(x1,y,color='blue')
plt.plot(x1,y_predict,color='red')
plt.scatter(lnwnon,non,color='black')
plt.show()

print("\n ===================================== \n")
print("ok")


