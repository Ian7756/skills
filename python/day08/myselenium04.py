from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver')
driver.get("http://localhost/HELLOWEB2/login.html")
driver.find_element_by_name('sabun').send_keys('1234')
driver.find_element_by_name('pwd').send_keys('1234')
driver.find_element_by_id('mybtn').click()
driver.implicitly_wait(3)

driver.get('http://localhost/HELLOWEB2/hello')
html = driver.page_source

tds = driver.find_elements_by_css_selector("td")

for td in tds:
    print(td.text)

