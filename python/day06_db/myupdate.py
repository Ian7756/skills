import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='java',
                       db='mypy', charset='utf8')
curs = conn.cursor()
sql = """update sample
         set col1 = '3',
             col2 = '6',
             col3 = '6'
           where col1 = '3'
             and col2 = '3'
             and col3 = '3' """
curs.execute(sql)
conn.commit()
conn.close()