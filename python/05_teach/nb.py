import pandas as pd

df = pd.read_csv('data/Fish.csv')
# print(df['Species'])
data_in = input("Spec : ")

data = df[data_in]

if data == "Bream":
    print("ok")