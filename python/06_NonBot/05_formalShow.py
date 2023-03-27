import pandas as pd
from tabulate import tabulate


# Create a sample DataFrame
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

# Format the DataFrame using tabulate
table = tabulate(df, headers='keys', tablefmt='psql',showindex=False)

print(table)