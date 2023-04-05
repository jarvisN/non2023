import numpy as np
import matplotlib.pyplot as plt
# from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import OneHotEncoder ,LabelEncoder

# สร้าง LabelEncoder
encoder = LabelEncoder()

df = pd.read_csv('data/Fish.csv')

# แปลงค่า categorical เป็นตัวเลข
numSpec = encoder.fit_transform(df['Species'])

# แสดงผลลัพธ์
print(numSpec.reshape(-1,1))









#  ======================= Test Zone ======================= 

# # กำหนดค่าให้แต่ละคำ
# species_mapping = {'Bream': 1, 'Parkki': 2, 'Perch': 3, 'Pike': 4, 'Roach': 5, 'Smelt': 6, 'Whitefish': 7}

# # แปลงค่าในคอลัมน์ Species เป็นตัวเลข
# df['Species'] = df['Species'].map(species_mapping)

# # สร้าง One-Hot Encoder
# encoder = OneHotEncoder()

# # ทำ One-Hot Encoding โดยใช้ค่าจากคอลัมน์ Species
# encoded_array = encoder.fit_transform(df[['Species']]).toarray()

# # สร้าง DataFrame จาก array ที่ถูก One-Hot Encoding แล้ว
# encoded_df = pd.DataFrame(encoded_array, columns=['Species_{}'.format(species) for species in species_mapping.values()])

# # แสดงผลลัพธ์
# print(encoded_df)

# print(df.head())


# print(df['Species'].head())

# # Create an instance of OneHotEncoder
# encoder = OneHotEncoder()

# # Fit the encoder on the DataFrame
# encoder.fit(df[['Species']])

# # Transform the DataFrame using the encoder
# encoded_df = pd.DataFrame(encoder.transform(df[['Species']]).toarray(), columns=encoder.get_feature_names_out(['Species']))

# # Print the encoded DataFrame
# print(encoded_df)



# # Access a single element using iloc
# print(df.iloc[0:, :])  # prints the value at row 0, column 1


# # Access a range of rows and columns using iloc
# print(df.iloc[0:5, 1:3])  # prints the first 5 rows and columns 1 and 2

# # Access a single column using iloc
# print(df.iloc[:, 4])  # prints all rows in column 4

# # Access a single row using iloc
# print(df.iloc[3, :])  # prints all columns in row 3

#  ======================= Test Zone =======================




def space():
    print('\n ==================================================== \n')
    
    