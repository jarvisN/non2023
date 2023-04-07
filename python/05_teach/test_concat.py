import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [5, 6, 7], 'D': [7, 8, 9]})
df3 = pd.DataFrame({'E': [10,11,12]})

# concatenate vertically
result1 = pd.concat([df1, df2], axis=0)

# concatenate horizontally
result2 = pd.concat([df1, df2], axis=1)
result3 = pd.concat([df1, df2,df3], axis=1)

# print(result1)
# print(result2)
print(result3)

