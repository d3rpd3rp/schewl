import sys, pickle, os
import pandas as pd
import rpy2.robjects as robjects
from datetime import datetime, timedelta
from requests import Request, Session, codes
from pandas.compat import StringIO
from collections import OrderedDict

def readSymbolsIntoPanda(filename):

    df = pd.read_csv(filename)

    npdf = pd.DataFrame(columns = df.columns)

    for index, row in df.iterrows():
        if ('NASDAQ'.lower() in str(row['Exchange']).lower()):
            npdf = npdf.append(row, ignore_index = True)
        else:
            None
    return (npdf)

def getEODdata(symbol, apiToken , s, begin, end, period):
    if s is None:
        s = Session()
        url = 'https://eodhistoricaldata.com/api/eod/' + str(symbol + '.US')
        #https://eodhistoricaldata.com/api/eod/MSFT.US?api_token=5cbfb658657909.68080282 
        paramsDict = {
            'from': begin,
            'to': end,
            'api_token': apiToken,
            'period': period
        }
        params = OrderedDict(paramsDict)
        #PREPARE
        req = Request('GET', url, params = params)
        prepreq = req.prepare()

        response = s.send(prepreq, stream=True, verify=True,\
            proxies=None, cert=None, timeout=60)

        if response.status_code == codes.ok:
            df = pd.read_csv(StringIO(response.text), skipfooter=1, parse_dates=[0], index_col=0)
            return df
        else:
            raise Exception(response.status_code, response.reason, url)
    else:
        print ('session established already.')
        return None

"""
?s=AAPL.US&api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&a=05&b=01&c=2017&d=10&e=02&f=2017&g=d
https://eodhistoricaldata.com/api/table.csv?s=AAPL.US&api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&a=05&b=01&c=2017&d=10&e=02&f=2017&g=d

https://eodhistoricaldata.com/api/table.csv?s=AAPL.US&api_token=5cbfb658657909.68080282&a=00&b=00&c=2018&d=01&e=20&f=2018&g=d

First of all, for yahoo-style you need to use another endpoint: https://eodhistoricaldata.com/api/table.csv.
For symbol you should use s, then for AAPL it will be: s=AAPL.US.
For ‘from date’ you should use a, b, c for month, day, year. Then 2017-01-05 will be: a=00, b=05, c=2017.
For ‘to date’ you should use d, e, f for month, day, year. Then 2017-02-10 will be: d=01, e=10, f=2017.
Please note, that in Yahoo! Finance API first months is 0 and last month (December) is 11. Then you need to substract 1 from months.
For ‘period’ you should use g. Possible values are d for daily, w for weekly and m for montly.
"""
def convertPDdftoRdf(pandasdf):
    #https://pandas.pydata.org/pandas-docs/version/0.22/r_interface.html
    if pandasdf is not None:
        #pandas2ri.activate()
        return robjects.py2ri(pandasdf)
    else:
        return None

def saveRobjects(someRobject):
    filename = str(someRobject + '_R_object_stock.pkl')
    with open(filename, 'wb') as output:
        pickle.dump(someObject, output, pickle.HIGHEST_PROTOCOL)
    output.close()


"""

    with open('company_data.pkl', 'rb') as input:
        company1 = pickle.load(input)
        print(company1.name)  # -> banana
        print(company1.value)  # -> 40

        company2 = pickle.load(input)
        print(company2.name) # -> spam
        print(company2.value)  # -> 42
"""


"""
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
"""

if __name__ == "__main__": 
    
    """
    npdf = readSymbolsIntoPanda(sys.argv[1])
    """

    #NEEDS ADJUSTED...DOES NOT ACCOUNT FOR MARKET CLOSURES
    #https://www.tutorialspoint.com/python3/time_strftime.htm
    #%w − day of the week as a decimal, Sunday = 0
    #%T − current time, equal to %H:%M:%S

    weekAgo = (datetime.today() - timedelta(days=9)).strftime('%Y-%m-%d')
    twoDaysAgo = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')

    go = '2018-01-02'
    stop = '2018-01-02'
    #stop = '2018-01-31'
    period = 'd'

    #rnpdf = pd.DataFrame(npdf.head(10))

    eodToken = ''
    s = None
    """
    print(rnpdf['Code'], type(rnpdf['Code']))
    
    for symbolString in rnpdf['Code']:
        #grab entire year / data set for each symbol
        vdf = getEODdata(symbolString, eodToken, s, go, stop, period)
    """
    """
    #single symbol test
    ssymbol = 'AAPL' 
    vdf = getEODdata(ssymbol, eodToken, s, go, stop, period)   
    print (vdf, type(vdf))

    #save sample pandas series
    vdf.to_pickle("./s-sample.pkl")
    """
    #load sample pandas series
    ssPdf = pd.read_pickle('./s-sample.pkl')
    print (ssPdf, type(ssPdf))

    #convert
    r_ssdf = convertPDdftoRdf(ssPdf)
    print (r_ssdf, type(r_ssdf))

    #save R objects

    #create table for each symbol (SQL)
    """
    for symbol in npdf['Code']:
        print (symbol, type(symbol))
        for index in range(0, 10):
            rnpdf = rnpdf.append(get_eod_data(symbol, 'US', start=go, end=stop, /\ 
                api_key=EOD_API_KEY, session=None))
        print ('breaking...')
        break

    for symbol in npdf['Code']:
        print (symbol, type(symbol))
        for index in range(0, 10):
            rnpdf = rnpdf.append(get_eod_data(symbol, 'US', \
                api_key=EOD_API_KEY, session=None))
        print ('breaking...')
        break
    
    print (rnpdf)

    rnpdf.to_csv(str(sys.argv[1]) + '.sample')
    """
    #100000 requests/day
else: 
    exit (None)