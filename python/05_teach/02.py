import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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

# x = x[selected_features][:130]
# y = y[:130]

x = x[selected_features]



# print(x.info)

# model.fit(x,y)



# print(f'score : {model.score(x,y)}')

#Check Score

a = []
b = []

for i in range(5,1300):
    # import time
    # print(i)
    # time.sleep(0.5)
    new_x = x[:i]
    new_y = y[:i]
    
   
    # print(new_x)
    
    model.fit(new_x,new_y)

    # if model.score(new_x, new_y) > 0.5:
        # print(f'score: {model.score(new_x, new_y)}, round: {i}')

    a.append(model.score(new_x, new_y))
    b.append(i)
    
    del new_x
    del new_y
    

    
# print(a)
# print(b)

plt.plot(b, a, color = "green")

# Add title and labels
plt.title("Score")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# Show plot
plt.show()