from binance import Client
import csv
from decouple import config

API_USERNAME = config('USER')
API_KEY = config('KEY')

client = Client(API_USERNAME, API_KEY)


def get_binance_bid_data():
    depth = client.get_order_book(symbol='BNBBTC').get('bids')
    print(depth)

    file = open('./data.csv', 'a', newline='')

    with file:
        write = csv.writer(file)
        write.writerow(depth)


def starter():
    get_binance_bid_data()
    starter()


starter()
