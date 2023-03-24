import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('data/data.csv')

# print(df.head())

# maxBedroom = df['bedrooms'].max()
# maxBathroom = df['bathrooms'].max()

# print(bedroom)

# print(type(len(bedroom)))

# print(f'max bedroom : {maxBedroom}')
# print(f'max bathroom : {maxBathroom}')

# x = df[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','sqft_above']]

# x = df.drop(['date','price','street','city','statezip','country'], axis=1)

x = df[['bedrooms','bathrooms','sqft_living']]

# x = df[['bedrooms','sqft_living']]
# print(X.head())

y = df['price']

# print(y.head())

model = LinearRegression()
data = model.fit(x,y)
print(data.coef_)


point = data.score(x,y)
print(point)


# # prediction

# result = model.predict([[2,0,0,0,0,0,0,0,0,0,2,1500]])

# print(result)

# plt.scatter(x, y)

plt.plot(x, model.predict(x), color='green')

# Add labels and a title to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Example')

# Show the plot
plt.show()