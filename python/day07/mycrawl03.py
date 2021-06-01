import requests
from bs4 import BeautifulSoup

response = requests.get("http://localhost/HELLOWEB2/hello")


bs = BeautifulSoup(response.text, 'html.parser')

tds = bs.select("td")

for td in tds:
    print(td.text)

