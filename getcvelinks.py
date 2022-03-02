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
    #print(f"{data}\r\n")
    for k,v in data.items():
      print(f"{k}:{v}\r\n")
