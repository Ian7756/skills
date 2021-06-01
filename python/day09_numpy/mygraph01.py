import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1,1,1,1,1]
y = [40,30,20,10,0]
y2 = [20,20,20,20,20]
y3 = [30,30,30,30,30]
y4 = [40,40,40,40,40]
z = [12,2,3,4,5]
plt.plot(x,y,'g',label='Enfield', linewidth=5)
# plt.plot(x,y2,'c',label='Honda',linewidth=5)
# plt.plot(x,y3,'r',label='Yahama',linewidth=5)
# plt.plot(x,y4,'y',label='KTM',linewidth=5)
plt.title('bike details in line plot')
plt.ylabel('Distance in kms')
plt.xlabel('Days')
plt.legend()
plt.show()