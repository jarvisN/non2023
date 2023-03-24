import pandas as pd

# create a sample DataFrame
data = {'name': ['John', 'Jane', 'Bob'], 'age': [25, 30, 35], 'city': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# save the DataFrame as a CSV file
df.to_csv('my_data.csv', index=False)
