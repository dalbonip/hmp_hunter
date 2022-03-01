import urllib.request
from bs4 import BeautifulSoup

def get_data(url):
  # url = "https://t.co/6jq4DIN7Z5"
  url_contents = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(url_contents, "lxml")
  div = soup.find("div", {"id": "GeneratedTable"})
  content = str(div)

  results = soup.findAll("td")
  
  datas = {}
  datas.update( [('CVE', results[8].get_text().strip()),('DATE',results[14].get_text().strip()),('DESCRIPTION',results[10].get_text().strip()),('EXTERNAL LINKS',results[12].get_text().strip())] )

  return datas

#x = 1
#for i in results:
#    print("\t",x)
#    print("\r\n")
#    content = i.get_text() # https://www.kite.com/python/answers/how-to-strip-text-from-an-html-string-in-python
#    print(content)
#    x = x+1