from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(1)

driver.get('http://localhost/HELLOWEB2/login')
driver.implicitly_wait(1)

driver.get('http://localhost/HELLOWEB2/hello')
html = driver.page_source


tds = driver.find_elements_by_css_selector("td")

for td in tds:
    print(td.text)

# tds = driver.find_elements_by_tag_name("td")
# for td in tds:
#     print(td.text)