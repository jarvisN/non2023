import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/data.csv')

x = df.drop(columns=['date','price','street','waterfront','view','city','statezip','country'])
y = df['price']

model = LinearRegression()
model.fit(x,y)

coeff_threshold = 500

feature_importance = pd.DataFrame({'feature': x.columns, 'importance': abs(model.coef_)})
selected_features = feature_importance[feature_importance['importance'] > coeff_threshold]['feature']

a = 123

x = x[selected_features][:a]
y = y[:a]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f'Training score: {train_score}')
print(f'Testing score: {test_score}')

new_data = pd.read_csv('data/data.csv')
x_new = new_data[selected_features]
y_pred = model.predict(x_new)
print(y_pred)

y_true = new_data['price']
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
