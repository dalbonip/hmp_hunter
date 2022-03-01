#/usr/bin/python3

import re
import json
from re import findall
import urllib.request
from bs4 import BeautifulSoup

from infromcve import get_data
#import pandas as pd
 
url1 = 'https://api.twitter.com/2/tweets/search/recent?query=from:CVEnew'
req1 = urllib.request.Request(url1, headers={'Authorization' : "Bearer AAAAAAAAAAAAAAAAAAAAAPs7ZQEAAAAAfDfpSvfaDAqtuIbAz9mBqaeXeWo%3Dp1mBM0Yj8FpU0nuXAdBDMlVPee3yXhRLy7ytro5Bk2MbkR10KY"})
con1 = urllib.request.urlopen(req1)
soup1 = BeautifulSoup(con1, "html.parser")

site_json=json.loads(soup1.text)
data_json = site_json['data']
for d in data_json:
  text = d.get('text')
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex,text)
  for x in url:
    data = get_data(x[0])
    print(f"{data}\r\n")



##initialize columns
#B = []
#C = []

###crawl through several pages with url & max number of pages
##def crawl(url, maxpage):
##    count = 1
##    while count < maxpage:
##        print("Crawling: " + url + str(count))
##        req = urllib.request.Request(url + str(count), headers={'User-Agent' : "Magic Browser"})
##        con = urllib.request.urlopen(req)
##        soup = BeautifulSoup(con, "html.parser")
##        #select table with required results
##        right_table=soup.find('div', {"id": 'search-results-box'})
##        neighborhood_div = right_table.findAll('div',{'class': 'listing-search-info font-size-85 overflow-ellipsis'})
##        #append neighborhood to B
##        for each in neighborhood_div:
##            neighborhood = each.contents
##            for item in neighborhood:
##                item = item.strip()
##                B.append(item)
##        #append prices to C
##        for row in right_table.findAll("tr"):
##            cells = row.findAll('td')
##            if len(cells)==2:
##               price_div = cells[0].find('div',{'class': 'color-fg-green'})
##               price = price_div.contents
##               for item in price:
##                   item = item.strip() #or item.replace('\n')
##                   C.append(item)
##        count += 1
##        df=pd.DataFrame(B, columns=['Neighborhood'])
##        df['Price']=C
##        df.to_csv('boston.csv')
##
##crawl("https://www.renthop.com/boston-ma/apartments-for-rent?page=",570)
