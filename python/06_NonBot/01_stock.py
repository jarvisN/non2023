# import RESTClient
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder

# create client
c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")


# get response
res = c.get_aggs("AAPL", 1, "day", "2023-03-22", "2023-03-24")


# Test 

# print(len(res))

# # print(res[0])
# # print(res[1])

# for i in range(len(res)):
#     print(res[i])