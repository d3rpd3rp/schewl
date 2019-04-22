#!/usr/bin/python3.6
#NEEEDS PAID ACCOUNT!!!!!
import newsapi
import json

apiO = newsapi.NewsApiClient(api_key='')

sourceList = ['bbc-news', 'the-verge', 'abc-news', 'crypto coins news', 'ary news','associated press',\
    'wired','aftenposten','australian financial review','axios',\
	'bbc news','bild','blasting news','bloomberg','business insider', 'google news',\
	'hacker news', 'info money', 'the next web','the verge']

pages = {}
pageNo = 1

while True:
    page = apiO.get_everything(language = 'en', to = '2018-12-31', from_param = '2018-01-01', \
        sources = sourceList, page = pageNo)
    if (~page):
        break
    else:
        pages[pageNo] = page
        pageNo += 1
