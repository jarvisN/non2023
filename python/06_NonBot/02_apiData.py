# import library
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder

# create client
c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

# get response
# res = c.get_aggs("AAPL", 1, "day", "2023-03-22", "2023-03-24")
res = c.get_aggs("C:XAUUSD", 1, "day", "2023-03-24", "2023-03-24")
print(res)


# Test 

# print(len(res))

print(f'open : {res[0].open}')
# print(f'open : {res[0].open}')

# for i in range(len(res)):
#     print(res[i])