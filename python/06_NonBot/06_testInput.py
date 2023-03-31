import pandas as pd
from polygon import RESTClient

from tabulate import tabulate

# create client
c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

# get response
res = c.get_aggs("C:XAUUSD", 1, "day", "2023-03-22", "2023-03-24")

# print(res)

# create list of dictionaries containing data for each time period
data = [{'Open': item.open, 'High': item.high, 'Low': item.low, 'Close': item.close, 'Volume': item.volume, 'VWAP': item.vwap, 'Timestamp': pd.to_datetime(item.timestamp/1000, unit='s'), 'Trade_ID': item.transactions} for item in res]

# create DataFrame from list of dictionaries
df = pd.DataFrame(data)

# print the resulting DataFrame
# print(df)


# Convert the DataFrame to a string
df_string = df.to_string()

# Format the DataFrame using tabulate
table = tabulate(df, headers='keys', tablefmt='psql')

print(f'```\n{table}\n```')