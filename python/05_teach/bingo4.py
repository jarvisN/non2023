from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv('data/diabetes.csv')

# print(df)
# print(df.columns.tolist())

x = df.drop(['DiabetesPedigreeFunction','Outcome'],axis=1)
y = df['Outcome']
# print(x)


X_train, X_test , y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)

# print(f'X Train : {X_train}')
# print(f'X Test : {X_test}')
# print(f'Y Train : {y_train}')
# print(f'Y Test : {y_test}')

# Create a logistic regreesion model
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)

# print(f'Score : {lr.score(X_train,y_train)}')

# Make predictions 
y_pred = lr.predict(X_test)

# calculate accuracy of the model

acc = accuracy_score(y_test,y_pred)

print(f'Accuracy : {acc}')

print("\n ========================================================== \n")

# Make predictions on test 

probs = lr.predict_proba(X_test)
probs_percent = probs * 100
for i in range(len(y_test)):
    print(f"Real Value : {y_test.iloc[i]} , Predicted Result : {y_pred[i]} ")
    print(f" 0 : {probs_percent[i][0]:.2f} % , 1 : {probs_percent[i][1]:.2f} %" )
    print("\n ========================================================== \n")



