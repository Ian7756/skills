# pip install PyMySQL
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                       db='mypy', charset='utf8')
curs = conn.cursor()
sql = """ delete from sample where col1='3' """
curs.execute(sql)
conn.commit()
conn.close()