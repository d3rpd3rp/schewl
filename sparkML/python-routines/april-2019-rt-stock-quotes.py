#!/usr/local/bin/python3.7
import sys
from googlefinance import getQuotes
from googlefinance import getNews

#https://github.com/hongtaocai/googlefinance/blob/master/googlefinance/
#__author__ = 'Hongtao Cai'
"""
googleFinanceKeyToFullName = {
    u'id'     : u'ID',
    u't'      : u'StockSymbol',
    u'e'      : u'Index',
    u'l'      : u'LastTradePrice',
    u'l_cur'  : u'LastTradeWithCurrency',
    u'ltt'    : u'LastTradeTime',
    u'lt_dts' : u'LastTradeDateTime',
    u'lt'     : u'LastTradeDateTimeLong',
    u'div'    : u'Dividend',
    u'yld'    : u'Yield',
    u's'      : u'LastTradeSize',
    u'c'      : u'Change',
    u'cp'      : u'ChangePercent',
    u'el'     : u'ExtHrsLastTradePrice',
    u'el_cur' : u'ExtHrsLastTradeWithCurrency',
    u'elt'    : u'ExtHrsLastTradeDateTimeLong',
    u'ec'     : u'ExtHrsChange',
    u'ecp'    : u'ExtHrsChangePercent',
    u'pcls_fix': u'PreviousClosePrice'
}
"""
symboldict = {}

with open(sys.argv[1], 'r') as symbolcsv:
    for line in symbolcsv.readlines():
        if line is not 'symbol':
            symboldict[line] = []
        else:
            None

symbolcsv.close()

for symbol in symboldict:
    print(type(symbol), symbol)


getQuotes(symboldict.keys())
getNews(symboldict.keys())