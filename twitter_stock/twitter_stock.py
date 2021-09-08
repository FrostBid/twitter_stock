"""Main module."""
from twitter import *
from yahoodata import *

symbol = str(input('Please input a stock symbol.')).upper()

yahoo = YahooData(symbol)
yahoo.historicalgraph()

stock = '$' + symbol
stock = TwitterData(stock)
stock.wordcloud()
stock.csv()
