import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
#This function doesnt work with str, just numbers
f = np.loadtxt("09_ADM_110.txt")
a = f[:,0:3]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(a[:,0],a[:,1],a[:,2])
color=cm.rainbow(np.linspace(0,1,len(a)))
x=y=z=x_sd=y_sd=z_sd = []
flag = []
for i in range (0,len(a),3):
    ax.scatter(a[i:i+3,0],a[i:i+3,1],a[i:i+3,2],c=color[i])
    # x = np.append(x,np.mean(a[i:i+3,0]))
    # x_sd = np.append(x_sd,np.std(a[i:i+3,0]))
    # y = np.append(y,np.mean(a[i:i+3,1]))
    # y_sd = np.append(y_sd,np.std(a[i:i+3,1]))
    # z = np.append(z,np.mean(a[i:i+3,2]))
    # z_sd = np.append(z_sd,np.std(a[i:i+3,2]))
plt.show()
f=0
#a=np.insert(a[0,:],0)
#w=np.append(a,np.linspace(1,len(a), len(a)), axis=1)
b=np.linspace(1,len(a), len(a))
b.reshape(60,1)
# for i in range (0,len(a)+1):
#a[0]=np.append(a[0],0)
print a


# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if i!=j:
#             ed = np.sqrt((a[i,0] - a[j,0])**2 +(a[i,1] - a[j,1])**2 + (a[i,2] - a[j,2])**2)


