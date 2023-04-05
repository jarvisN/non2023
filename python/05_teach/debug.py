import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# create a LabelEncoder instance
encoder = LabelEncoder()

# read the CSV file into a pandas dataframe
df = pd.read_csv('data/Fish.csv')

# encode the 'Species' column using LabelEncoder
df['numSpec'] = encoder.fit_transform(df['Species'])

# show the resulting dataframe
print(df.head)
