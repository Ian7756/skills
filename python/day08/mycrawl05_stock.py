import requests
from bs4 import BeautifulSoup
from nltk.util import pr
from datetime import date, datetime, time
import pymysql
import time

cnt = 0
while cnt < 10: 
    response = requests.get("https://www.sedaily.com/Stock/Quote/?mobile")
    bs = BeautifulSoup(response.text, 'html.parser')
    tags = bs.find_all(class_="tbody")
    for tag in tags:
        s_code = tag.dd['id'].replace("dd_Item_","")
        s_name = tag.dt.a['title']
        s_price = tag.span.text.replace(",","")
        s_time =  datetime.today().strftime('%Y%m%d.%H%M')
        conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                               db='mypy', charset='utf8')
        sql = """insert into stock(s_code,s_name,s_price,s_time)
                 values (%s, %s, %s, %s)"""
        curs = conn.cursor()
        curs.execute(sql, (s_code, s_name, s_price,s_time))
        conn.commit()
        conn.close()
    time.sleep(60)
    cnt += 1
    print(cnt)


#DATE_FORMAT(now(),'%Y%m%d.%H%i'))
