import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1,1,1,1,1,1,1,1,1,1]
x1 = [2,2,2,2,2,2,2,2,2,2]
x2 = [3,3,3,3,3,3,3,3,3,3]
x3 = [4,4,4,4,4,4,4,4,4,4]
y = range(10)

z = [85900,86000,85900,86000,85900,85900,85800,85800,85700,85700]

z1 = [90100,90200,90000,90100,90000,90000,90000,90000,90000,90000]

z2 = [243000,242500,243000,242500,242500,242500,242500,242500,242500,242500]

z_init = z[0]/100
z1_init = z1[0]/100
z2_init = z2[0]/100

for i,item in enumerate(z):
    z[i] = z[i]/z_init
    z1[i] = z1[i]/z1_init
    z2[i] = z2[i]/z2_init



plt.plot(x,y,z,'g',label='samsung', linewidth=5)
plt.plot(x1,y,z1,'r',label='gia', linewidth=5)
plt.plot(x2,y,z2,'b',label='hundai', linewidth=5)
plt.legend()
plt.show()
