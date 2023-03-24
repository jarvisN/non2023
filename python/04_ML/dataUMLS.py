import pandas as pd

df = pd.read_csv('data/DiseaseData.csv')

# print(df)

# topic = df.columns.tolist()
# print(topic)

symptom = df['Symptom']
# print(symptom)


buffer = []
umlsCode = []
lstSymptom = []

def checkData():
    test = df['Symptom']
    # print(test)
    for i in range(len(test)):
        if pd.isna(df['Symptom'][i]) or None or "":
            print(f'address : {i} , value : {test[i]} type : {type(test[i])} ')
            break

for i in range(len(symptom)):
    data = df['Symptom'][i]
    if isinstance(data, str): # Check if data is a string
        dataSplit = data.split("^")
        if len(dataSplit) > 1 : 
            for j in range(len(dataSplit)):
                buffer.append(dataSplit[j])
        else:
            buffer.append(data)
            
# Before set
# print(buffer)
# print(len(buffer))

# print(len(symptom))

# After set
buffer = list(set(buffer))
# print(len(buffer))
# print(buffer)

# print(buffer[0])


for i in range(len(buffer)):
    # print(buffer[i].split("_"))
    a = buffer[i].split("_")[0]
    b = buffer[i].split("_")[1]
    # print(b) # symptom
    
    c = buffer[i].split("_")[0].split(":")[1]
    # print(c) # UMLS code
    
    
    lstSymptom.append(b)
    umlsCode.append(c)

# print(lstSymptom)
# print(umlsCode)

createCSV = pd.DataFrame({
    'UMLS': umlsCode,
    'Symptom': lstSymptom
})

print(createCSV)

createCSV.to_csv('datasetSympotom_umls.csv', index=False)

print("Done")