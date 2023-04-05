import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value': [4, 5, 6]})

# inner join
result3 = pd.merge(df1, df2, on='key', how='inner')

# outer join
result4 = pd.merge(df1, df2, on='key', how='outer')

# print(result3)
# print(result4)