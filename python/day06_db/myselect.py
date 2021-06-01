import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                       db='mypy', charset='utf8')
curs = conn.cursor()
sql = "select * from sample"
curs.execute(sql)
rows = curs.fetchall()
print(rows[0][0])
conn.close()

