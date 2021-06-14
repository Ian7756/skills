import pymysql

# insert 
conn = pymysql.connect(host='127.0.0.1', user='root', password='java', db='mypy', charset='utf8')

curs = conn.cursor()
sql = """insert into sample(col1,col2,col3)
         values (%s, %s, %s)"""
curs.execute(sql, ('4', '4', '4'))
conn.commit()
conn.close()

# select


# update


# delete