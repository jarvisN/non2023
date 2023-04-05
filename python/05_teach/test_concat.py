import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})

# concatenate vertically
result1 = pd.concat([df1, df2], axis=0)

# concatenate horizontally
result2 = pd.concat([df1, df2], axis=1)

# print(result1)
print(result2)


