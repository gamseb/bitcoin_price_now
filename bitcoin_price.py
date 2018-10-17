#!/usr/bin/python

#This is a script that returns the price of one Bitcoin in US dollars
import requests, json

#Gets the api of https://www.bitcoinprice.com
response = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&e=CCCAGG")
#Converts to json
a = response.json()
#prints to the console
print("*" * 30)
print("The current price of one bitcoin is:")
print("{} USD".format(a['RAW']['BTC']['USD']['PRICE']))
