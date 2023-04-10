import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

model = SVC()

# create a LabelEncoder instance
encoder = LabelEncoder()

# read the CSV file into a pandas dataframe
df = pd.read_csv('data/Fish.csv')

# encode the 'Species' column using LabelEncoder
df['numSpec'] = encoder.fit_transform(df['Species'])

X = df[['Width','Height']]
y = df['numSpec']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=66)

x_train_array = X_train.to_numpy().reshape(-1,2)
y_train_array = y_train.to_numpy().reshape(-1,)

model.fit(x_train_array, y_train_array)

print(model.score(X_test, y_test))

# print("\n =============================== \n")

# X_new = np.array([[10, 20]])
# y_pred = model.predict(X_new)
# print(y_pred)

print(df['numSpec'])
print(df['Species'])