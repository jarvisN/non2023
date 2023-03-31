import pandas as pd
from datetime import datetime
from polygon import RESTClient
from tabulate import tabulate

# create client
c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

ticket = input("Ticket : ").upper()
unit = input("Unit : ")
dayStart = input("Day : ")
dayStop = input("Day (leave blank for current time) : ")

# set current time if dayStop is not provided
if dayStop == "":
    dayStop = datetime.now().strftime("%Y-%m-%d")

# get response
res = c.get_aggs(f"C:{ticket}", 1, f"{unit}", f"{dayStart}", f"{dayStop}")

# create list of dictionaries containing data for each time period
data = [{'Open': item.open, 'High': item.high, 'Low': item.low, 'Close': item.close, 'Volume': item.volume, 'VWAP': item.vwap, 'Timestamp': pd.to_datetime(item.timestamp/1000, unit='s'), 'Transactions': item.transactions} for item in res]

# create DataFrame from list of dictionaries
df = pd.DataFrame(data)

# Convert the DataFrame to a string
df_string = df.to_string()

# Format the DataFrame using tabulate
table = tabulate(df, headers='keys', tablefmt='psql')

print(f'```\n{table}\n```')
