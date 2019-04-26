"""
In [1]: import pandas as pd
In [2]: pd.set_option("max_rows", 10)
In [3]: from eod_historical_data import get_eod_data
In [4]: df = get_eod_data("AAPL", "US")
In [5]: df
"""
"""
10	Indexes	INDX
11	USA Stocks	US
16	London Exchange	LSE
19	NSE (India)	NSE
20	Hong Kong Exchange	HK
21	Borsa Italiana	MI
22	SIX Swiss Exchange	SW
23	Hamburg Exchange	HM
24	Toronto Exchange	TO
34	Euronext Brussels	BR
39	London IL	IL
"""
import sys
from datetime import datetime, timedelta
from eod_historical_data import get_eod_data
import pandas as pd

EOD_API_KEY=''

def readSymbolsIntoPanda(filename):

    df = pd.read_csv(filename)

    npd = pd.DataFrame(columns = df.columns)

    for index, row in df.iterrows():
        if ('NASDAQ'.lower() in str(row['Exchange']).lower()):
            npd = npd.append(row, ignore_index = True)
        else:
            None
    return (npd)

npd = readSymbolsIntoPanda(sys.argv[1])

print (npd)

#NEEDS ADJUSTED...DOES NOT ACCOUNT FOR MARKET CLOSURES
go = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
stop = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
"""
for symbol in npd['Code']:
    rnpd = get_eod_data(symbol, 'US', start=go, end=stop, \
    api_key=EOD_API_KEY, session=None)

print (df)
"""

#100000 requests/day