# import library
import pandas as pd
from tabulate import tabulate
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder

# # create client
# c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

# # get response
# # res = c.get_aggs("AAPL", 1, "day", "2023-03-22", "2023-03-24")
# res = c.get_aggs("C:XAUUSD", 1, "day", "2023-03-23", "2023-03-24")
# print(res)

# print("\n ================================================= \n")
# # print(res[0])

# for i in range(len(res)):
#     print(f'Round : {i+1}')
#     print(res[i])
#     print("\n ================================================= \n")


# print(f'open : {res[0].open}')


# # Create a sample DataFrame
# df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

# # Format the DataFrame using tabulate
# table = tabulate(df, headers='keys', tablefmt='psql',showindex=False)

# print(table)