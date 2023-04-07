import numpy as np
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
from sklearn import svm
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create a LabelEncoder instance
encoder = LabelEncoder()

# read the CSV  file into a pandas dataframe
df = pd.read_csv('data/Fish.csv')

# encode the 'Species' column using LabelEncoder
df['numSpec'] = encoder.fit_transform(df['Species'])


# show the resulting dataframe
# print(df.head)

x1 = df['Weight']
x2 = df['Height']

# print(x2)

X = pd.concat([x1, x2], axis=1)
y = df['numSpec']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=66)

# print(f'X Train : {X_train}')
# print(f'X Test : {X_test}')
# print(f'y Train : {y_train}')
# print(f'y Test : {y_test}')

clf = svm.SVC(kernel='linear', C=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# print(y_pred)


accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)





def space():
    print('\n ==================================================== \n')
    
    