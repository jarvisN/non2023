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
y2 = df['SAT'].values.reshape(-1,1)

# print(x)

# print("\n ===================================== \n")

# print(y)

# plt.scatter(x,y)
# plt.show()

# print("\n ===================================== \n")




pl = PolynomialFeatures(degree=33)
x_pl = pl.fit_transform(x1)

model = LinearRegression()
model.fit(x_pl,y)

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



non = input("Enter: ")

non = float(non)


# # Transform the input value into a polynomial feature array of degree 33
x_new = pl.transform([[non]])
# print(x_new)
# Predict with the model using the transformed input value
y_predict = model.predict(x_pl)
y_predict_new = model.predict(x_new)




# Plot the original scatter plot, regression line, and predicted value for the new input
plt.scatter(x1,y,color='blue')
plt.scatter(non, y_predict_new, color='green')
plt.plot(x1,y_predict,color='red')
plt.show()

print("\n ===================================== \n")
print("ok")


