#!/home/gamseb/anaconda3/bin/python3

#This is a script that returns the price of one Bitcoin in US dollars
import requests, json

#Gets the api of https://www.bitcoinprice.com and converts it to json
usd = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&e=CCCAGG").json()
euro = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=EUR&e=CCCAGG").json()
#Gets the bitcoin symbol
bitcoin_symbol = usd['DISPLAY']['BTC']['USD']['FROMSYMBOL']
#prints to the console
print("*" * 36)
print("The current price of one {}itcoin is:".format(bitcoin_symbol))
print("{} USD".format(usd['RAW']['BTC']['USD']['PRICE']))
print("{} EUR".format(euro['RAW']['BTC']['EUR']['PRICE']))
print("*" * 36)

