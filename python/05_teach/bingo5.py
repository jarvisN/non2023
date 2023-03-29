import pandas as pd
import time
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/weatherHistory.csv')

# print(df.head())

x = df.drop(['Formatted Date', 'Daily Summary', 'Summary',
            'Precip Type', 'Loud Cover'], axis=1)

# print(data)


print("\n ====================================== \n")


# create an instance of OneHotEncoder
encoder = OneHotEncoder()

# fit and transform the dataframe
encoded_data = encoder.fit_transform(df[['Precip Type']])


# create a new dataframe from the encoded data
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(['Precip Type']))

# concatenate the original dataframe and the encoded dataframe
# final_df = pd.concat([df, encoded_df], axis=1)

# display the final dataframe
# print(final_df)


y = encoded_df.drop(['Precip Type_nan','Precip Type_snow'], axis=1)


# print("\n ====================================== \n")

# print(y)

# y.to_csv('example.csv', index=False)

# print("\n ====================================== \n")


# print("\n ====================================== \n")

# # final_df = pd.concat([data, encoded_df], axis=1)
# # print(final_df)


# # Logistic Regression

# # print(data)
# # print(final_df)

# # print(encoded_df)

X_train, X_test , y_train, y_test = train_test_split(x,y,train_size=0.3,random_state=42)

# print(f'X Train : {X_train}')
# print(f'X Test : {X_test}')
# print(f'Y Train : {y_train}')
# print(f'Y Test : {y_test}')



lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)

# print(f'Score : {lr.score(X_train,y_train)}')

y_pred = lr.predict(X_test)
acc = accuracy_score(y_test,y_pred)
# print(f'Acc :{acc}')

print("\n ====================================== \n")



probs = lr.predict_proba(X_test)

# print(probs)

probs_percent = probs * 100
# print(probs_percent)





for i in range(len(y_test)):
    print(f"Real Value : {y_test['Precip Type_rain'].iloc[i]} , Predicted Result : {y_pred[i]} ")
    print(f" 0 : {probs_percent[i][0]:.2f} % , 1 : {probs_percent[i][1]:.2f} %" )
    print("\n ==========================================\n")
    time.sleep(1)

print("\n ====================================== \n")
print("ok")

