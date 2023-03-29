# import library
import pandas as pd
from tabulate import tabulate
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder


# create client
c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

# get response
res = c.get_aggs("C:XAUUSD", 1, "day", "2023-03-22", "2023-03-24")

# create list of dictionaries containing data for each time period
data = [{'Open': item.open, 'High': item.high, 'Low': item.low, 'Close': item.close, 'Volume': item.volume,
         'VWAP': item.vwap, 'Timestamp': item.timestamp, 'Transactions': item.transactions} for item in res]

# create DataFrame from list of dictionaries
df = pd.DataFrame(data)

# print the resulting DataFrame
print(df)


# Format the DataFrame using tabulate
table = tabulate(df, headers='keys', tablefmt='psql', showindex=False)

print(table)
