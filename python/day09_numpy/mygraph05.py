import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pymysql


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


conn = pymysql.connect(host='127.0.0.1', user='root', password='java', db='mypy', charset='utf8')
curs = conn.cursor()

#sql = "select distinct s_name from stock"
#curs.execute(sql)
#rows = curs.fetchall()
#myarr = np.reshape(rows,(len(rows)))

myarr = ["삼성전자","현대차","기아차","SK하이닉스"]
for i,s_name in enumerate(myarr):
    sql = """select s_price from stock2 where s_name = %s order by s_time"""
    curs.execute(sql,s_name)
    rows = curs.fetchall()
    s_price = np.reshape(rows,(len(rows)))
    z = np.zeros((len(s_price)))
    z_init = int(s_price[0])/100

    for j,item in enumerate(z):
        z[j] = int(s_price[j])/z_init
    
    plt.plot(np.ones((len(s_price)))+i,range(len(s_price)),z,label=i, linewidth=2)

conn.close()
plt.legend()
plt.show()
