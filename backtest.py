#%%
import talib
from zipline.api import order_target, record, symbol, order_target_percent

'''   
This example algorithm uses the Relative Strength Index indicator as a buy/sell signal.
When the RSI is over 70, a stock can be seen as overbought and it's time to sell.
When the RSI is below 30, a stock can be seen as oversold and it's time to buy.
'''

# Setup our variables
def initialize(context):
    
    # what stock to trade - FAANG in this example
    # stocklist = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']
    stocklist = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']

    # make a list of symbols for the list of tickers
    context.stocks = [symbol(s) for s in stocklist]
    
    # create equal weights of each stock to hold in our portfolio
    context.target_pct_per_stock = 1.0 / len(context.stocks)
    
    # create initial RSI threshold values for low (oversold and buy signal) and high (overbought and sell signal)
    context.LOW_RSI = 30
    context.HIGH_RSI = 70

# Rebalance daily.
def handle_data(context, data):
    
    # Load historical pricing data for the stocks, using daily frequncy and a rolling 20 days
    prices = data.history(context.stocks, 'price', bar_count=20, frequency="1d")
    
    rsis = {}
    
    # Loop through our list of stocks
    for stock in context.stocks:
        # Get the rsi of this stock.
        rsi = talib.RSI(prices[stock], timeperiod=14)[-1]
        rsis[stock] = rsi
        
        current_position = context.portfolio.positions[stock].amount
        
        # RSI is above 70 and we own shares, time to sell
        if rsi > context.HIGH_RSI and current_position > 0 and data.can_trade(stock):
            order_target(stock, 0)
   
        # RSI is below 30 and we don't have any shares, time to buy
        elif rsi < context.LOW_RSI and current_position == 0 and data.can_trade(stock):
            order_target_percent(stock, context.target_pct_per_stock)

    # record the current RSI values of each stock for later ispection
    record(fb_rsi=rsis[symbol('FB')],
           amzn_rsi=rsis[symbol('AMZN')],
           aapl_rsi=rsis[symbol('AAPL')],
           nflx_rsi=rsis[symbol('NFLX')],
           googl_rsi=rsis[symbol('GOOGL')])