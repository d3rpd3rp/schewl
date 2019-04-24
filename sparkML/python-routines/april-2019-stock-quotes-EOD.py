"""
In [1]: import pandas as pd
In [2]: pd.set_option("max_rows", 10)
In [3]: from eod_historical_data import get_eod_data
In [4]: df = get_eod_data("AAPL", "US")
In [5]: df
"""
from datetime import datetime, timedelta
from eod_historical_data import get_eod_data

EOD_API_KEY=''


#NEEDS ADJUSTED...DOES NOT ACCOUNT FOR MARKET CLOSURES
go = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
stop = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')

symbol = 'GOOGL'

print (go, stop)

df = get_eod_data(symbol, 'US', start=go, end=stop, \
    api_key=EOD_API_KEY, session=None)

print (df)

