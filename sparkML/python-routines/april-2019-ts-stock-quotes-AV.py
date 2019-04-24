#!/usr/local/bin/python3.6
import json,sys
import pandas
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='HVRKST0RUEEC0OQ3', output_format = 'pandas', indexing_type='integer')
# Get json object with the intraday data and another with  the call's metadata
i = 1
with open(sys.argv[1], 'r') as symbolcsv:
    while ( i < 6): 
        for line in symbolcsv.read().splitlines():
            if 'symbol' not in line and line != None:
                print (repr(line), type(line))
                try: 
                    symboldata, mdata = ts.get_intraday(symbol = line)
                except:
                    print('issue with query.')
            else:
                None
            i += 1

symbolcsv.close()
