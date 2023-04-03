from flask import Flask,jsonify,request
import pandas as pd
from polygon import RESTClient
import socket
from tabulate import tabulate
import datetime


app = Flask(__name__)

deBug = []


@app.route("/")
def home():
    return "Hello, from Flask!"

@app.route('/myapi', methods=['POST'])
def myapi():
    data = request.get_json()
    print(data)
    # process the data as needed
    return 'Success'




@app.route('/ask', methods=['POST'])
def price():
    
    data = request.get_json()
    print(data)
    print("\n ================================ \n")
    
    ticket = data['Ticket']
    day_start = data['DayStart']
    day_stop = data['DayStop']
    unit = data['UniT']
    
    # Check if day_start has a year
    if len(day_start) < 6:
        current_year = datetime.datetime.now().year
        day_start = f"{current_year}-{day_start}"

    # Check if day_stop has a year
    if len(day_stop) < 6:
        current_year = datetime.datetime.now().year
        day_stop = f"{current_year}-{day_stop}"
        
    
    
    # create client
    c = RESTClient(api_key="sgI3UObKfOdY6Esk6_Z77g6rfnPpUgZx")

    # get response
    res = c.get_aggs(f'C:{ticket}', 1, f'{unit}', f'{day_start}', f'{day_stop}')

    # create list of dictionaries containing data for each time period
    data = [{'Open': item.open, 'High': item.high, 'Low': item.low, 'Close': item.close, 'Volume': item.volume, 'VWAP': item.vwap, 'Timestamp': pd.to_datetime(item.timestamp/1000, unit='s'), 'Transactions': item.transactions} for item in res]

    # create DataFrame from list of dictionaries
    df = pd.DataFrame(data)
    
    # Format the DataFrame using tabulate
    table = tabulate(df, headers='keys', tablefmt='psql')
    
    print(f'```\n{table}\n```')
    non = f'```\n{table}\n```'
    
    return non

if __name__ == "__main__":
    app.run()
