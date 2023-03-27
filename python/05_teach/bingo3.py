import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


DB = pd.read_csv('data/bingo.csv')



x = DB['X'].values.reshape((-1, 1))
y = DB['Y']

lr = LinearRegression()

data = lr.fit(x,y)



new_x = np.array(x).reshape((-1, 1))


d = lr.predict(new_x)

print(d)


dc=pd.concat([DB.reset_index(),pd.Series(d, name='predicted')], axis='columns')
print(dc)

