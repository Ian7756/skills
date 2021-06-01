import os
import sys
import urllib.request
from bs4 import BeautifulSoup

client_id = "tJiTH69WDM9qavtok_AF"
client_secret = "xGe8myF9mg"
encText = urllib.parse.quote("대전맛집")
# url = "https://openapi.naver.com/v1/search/local.xml?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
else:
    print("Error Code:" + rescode)


html = response_body.decode('utf-8')

bs = BeautifulSoup(html, 'html.parser')
#bs = BeautifulSoup(xml, 'xml')

#print(bs.find_all("item"))
# item = bs.item

# print(item.title.text)
# print(item.mapx.contents[0])
# print(item.mapy.contents[0])

for item in bs.find_all("item"):
    print(item.title.text)




