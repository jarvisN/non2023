import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Convert the DataFrame to a string
df_string = df.to_string()

print(df_string)

print("\n ================================================= \n")


# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Convert the DataFrame to a string with a tabular format
table_string = df.to_string(index=False, justify='left')

print(table_string)


print("\n ================================================= \n")


from tabulate import tabulate

# Create a sample DataFrame
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

# Format the DataFrame using tabulate
table = tabulate(df, headers='keys', tablefmt='psql')

print(table)


# # Send the table as a message using Nextcord
# await interaction.send(f'```\n{table}\n```')