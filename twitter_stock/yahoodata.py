import yfinance as yf
import plotly.graph_objects as plgo
import sys


class YahooData():
    def __init__(self, stock):
        if (yf.Ticker(stock).info['regularMarketPrice'] == None):
            print(f"ERROR: {stock} is not a valid stock, please try again.")
            sys.exit(1)
        self.stock = yf.Ticker(stock)
        print('Fetching stock data from yahoo.')

    def historicalgraph(self):
        df = self.stock.history(period="max")
        df = df.reset_index()
        for i in ['Open', 'High', 'Close', 'Low']:
            df[i] = df[i].astype('float64')

        fig = plgo.Figure([plgo.Scatter(x=df['Date'], y=df['High'])])
        fig = plgo.Figure(data=[plgo.Candlestick(x=df['Date'],
                                                 open=df['Open'],
                                                 high=df['High'],
                                                 low=df['Low'],
                                                 close=df['Close'])])

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        fig.show()
        fig.write_image(f"{self.stock.info['symbol']}_stockprice.png")

        print('Stock data compiled.')
