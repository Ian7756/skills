# pip install PyMySQL
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='java', db='mypy', charset='utf8')
curs = conn.cursor()
sql = """insert into sample(col1,col2,col3)
         values (%s, %s, %s)"""
         
curs.execute(sql, ('4', '4', '4'))

conn.commit()
conn.close()

# select

sql = "select * from sample"
curs.execute(sql)
rows = curs.fetchall()
print(rows[0][0])
conn.close()

# update
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

# delete

sql = """ delete from sample where col1='3' """
curs.execute(sql)
conn.commit()
conn.close()