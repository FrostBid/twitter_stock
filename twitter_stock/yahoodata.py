import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io

class YahooData(self,stock):
    def __init__(self):
        self.stock = stock

    def getdata(stock):
        # create empty dataframe
        stock_final = pd.DataFrame()
        # iterate over each symbol
        for i in Symbols:

            # print the symbol which is being downloaded
            print(str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)

            try:
                # download the stock price
                stock = []
                stock = yf.download(i, start=start, end=end, progress=False)

                # append the individual stock prices
                if len(stock) == 0:
                    None
                else:
                    stock['Name'] = i
                    stock_final = stock_final.append(stock, sort=False)
            except Exception:
                None
