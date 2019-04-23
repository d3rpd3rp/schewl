#!/usr/bin/python3.6
import newsapi
import json

apiO = newsapi.NewsApiClient(api_key='')

sourceList = 'bbc-news,the-verge,abc-news,crypto coins news,ary news,associated press,\
    wired,aftenposten,australian financial review,axios,\
	bbc news,bild,blasting news,bloomberg,business insider,google news,\
	hacker news,info money,the next web,the verge'

pages = {}
pageNo = 1

while True and pageNo < 100:
    page = apiO.get_everything(language = 'en', from_param = '2019-03-23', \
        sort_by = 'popularity', sources = sourceList, page = pageNo)
    print(page, type(page))
    if not page:
        break
    else:
        pages[pageNo] = page
        pageNo += 1
