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
from requests import Request, Session
from eod_historical_data import get_eod_data
import pandas as pd

EOD_API_KEY=''

def readSymbolsIntoPanda(filename):

    df = pd.read_csv(filename)

    npdf = pd.DataFrame(columns = df.columns)

    for index, row in df.iterrows():
        if ('NASDAQ'.lower() in str(row['Exchange']).lower()):
            npdf = npdf.append(row, ignore_index = True)
        else:
            None
    return (npdf)


def sendDataframes(dataframe, remoteHost, localHostSCert):

    s = Session()

    req = Request('POST', remoteHost, data=data, headers=headers)
    prepped = req.prepare()

    # do something with prepped.body
    prepped.body = 'No, I want exactly this as the body.'

    # do something with prepped.headers
    del prepped.headers['Content-Type']

#https://2.python-requests.org//en/master/user/advanced/#keep-alive
#Note that connections are only released back to the pool for reuse 
#once all body data has been read; be sure to either set stream to False 
#or read the content property of the Response object.

    resp = s.send(prepped,
        stream = True,
        verify = False,
        proxies = False,
        cert = localHostSCert,
        timeout = -1
    )

    print(resp.status_code)

if __name__ == "__main__": 
    
    npdf = readSymbolsIntoPanda(sys.argv[1])

    print (npdf)

    #NEEDS ADJUSTED...DOES NOT ACCOUNT FOR MARKET CLOSURES
    #https://www.tutorialspoint.com/python3/time_strftime.htm
    #%w − day of the week as a decimal, Sunday = 0
    #%T − current time, equal to %H:%M:%S

    go = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
    stop = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
    """
    for symbol in npdf['Code']:
        rnpdf = get_eod_data(symbol, 'US', start=go, end=stop, \
        api_key=EOD_API_KEY, session=None)

    print (df)
    """

    #small test

    rnpdf = pd.DataFrame(npdf.head(10))

    """
    for symbol in npdf['Code']:
        print (symbol, type(symbol))
        for index in range(0, 10):
            rnpdf = rnpdf.append(get_eod_data(symbol, 'US', start=go, end=stop, /\ 
                api_key=EOD_API_KEY, session=None))
        print ('breaking...')
        break
    """
    for symbol in npdf['Code']:
        print (symbol, type(symbol))
        for index in range(0, 10):
            rnpdf = rnpdf.append(get_eod_data(symbol, 'US', \
                api_key=EOD_API_KEY, session=None))
        print ('breaking...')
        break

    print (rnpdf)

    rnpdf.to_csv(str(sys.argv[1]) + '.sample')

    #100000 requests/day
else: 
    exit