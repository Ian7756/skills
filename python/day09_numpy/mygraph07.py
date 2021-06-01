import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='java', db='_stock_old', charset='utf8')
curs = conn.cursor()

def getPrice():
    sql = "select s005930,s000270,s001500,s000660 from stock order by in_time limit 10"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows

fig = plt.figure(figsize=(19,9))
ax = fig.add_subplot(1,1,1, projection='3d')
plt.title("Stock Price")
plt.xlabel("company")
plt.ylabel("days")
sql = "SELECT  COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'STOCK' AND  COLUMN_NAME NOT LIKE 'in_time'"
curs.execute(sql)
rows = curs.fetchall()
col_name = np.reshape(rows,(len(rows)))
#col_name = ["s005930","s000270","s001500","s000660"]


s_price = getPrice()
print(np.reshape(s_price),(len(s_price[0]),len(s_price)))

# for i,s_name in enumerate(col_name):
#     s_price = getPrice(s_name)
#     
#     z = np.zeros((len(s_price)))
#     
#     for j,item in enumerate(z):
#         if int(s_price[j]) != 0:
#             z[j] = (int(s_price[j])/int(s_price[0])) * 100
#         else:
#             z[j] = int(s_price[j])
# 
# 
# plt.plot(np.ones((len(s_price)))+i,range(len(s_price)),z,label=s_name, linewidth=1)
# 
# conn.close()
# #plt.legend()
# plt.show()


