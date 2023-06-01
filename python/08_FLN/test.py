import pandas as pd
import numpy as np
from sklearn import linear_model
species=input()
df = pd.read_csv('Fish.csv')
df = df.drop(['Length1', 'Length2', 'Length3'], axis='columns')

fish_rows = df[df['Species'] == species]
x=int(input())
y=int(input())
reg = linear_model.LinearRegression()
reg.fit(fish_rows.drop(['Species', 'Weight'], axis='columns'), fish_rows['Weight'])
print(reg.predict([[x,y]]))