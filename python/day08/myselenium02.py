from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(1)

driver.get('http://localhost/HELLOWEB2/login')
driver.implicitly_wait(1)

driver.get('http://localhost/HELLOWEB2/hello')
html = driver.page_source

bs = BeautifulSoup(html, 'html.parser')

tags = bs.select('td')
for tag in tags:
    print(tag.text)
