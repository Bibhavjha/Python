import matplotlib.pyplot as plt
import numpy as np
# x=np.array([5,7,8,7])
# y=np.array([99,86,87,88])
# colors=np.array([0,10,20,30,40,45,50,55,60,70,80,90,10])
# colors=np.array(["red","green","blue",'yellow'])
# plt.scatter(x,y,c=colors,cmap='virdis')
# plt.colorbar()
# plt.show()

# changing size of dots 
# x=np.array([5,7,8,7])
# y=np.array([99,86,87,88])
# sizes=([20,50,100,200])
# colors=np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
# colors=np.array(["red","green","blue",'yellow'])
# plt.scatter(x,y,s=sizes,c=colors,cmap='virdis')
# plt.colorbar()
# plt.show()

# alpha attribute to change the transparency
x=np.array([5,7,8,7])
y=np.array([99,86,87,88])
sizes=([20,50,100,200])
colors=np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
colors=np.array(["red","green","blue",'yellow'])
plt.scatter(x,y,s=sizes,c=colors,cmap='virdis',alpha=0.5)
plt.colorbar()
plt.show()


