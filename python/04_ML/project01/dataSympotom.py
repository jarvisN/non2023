import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('data/rawData.csv')

# Display the DataFrame
# print(df)

symptom = df.columns.tolist()

# print(symptom)
# print(len(symptom))
# print(type(symptom))

#Get Symptom Columns 
TopicSymptom = symptom[:-2]
# print(TopicSymptom)
# print(type(TopicSymptom[0]))


#Single row < First row > 

valueSympotom = df.iloc[0:1,:-2]
# print(valueSympotom)

col = valueSympotom.columns.tolist()
# print(col)
symptom1 = []


for i in range(len(col)):
    # print(col[i])
    data = df[col[i]].iloc[0:1][0]
    # print(data)
    aaa = df[col[i]].iloc[0:1].name
    print(aaa)
    if data == 1 :
        # print(df[col[i]].iloc[0:1].name)
        symptom1.append(df[col[i]].iloc[0:1].name)

# print(symptom1)

# print(df[symptom1].iloc[0:1])

# chart = df[symptom1].iloc[0:1].plot(kind = 'bar')
# plt.show()


print("==================================")
print("End")
print("==================================")