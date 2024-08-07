import matplotlib.pyplot as plt
import numpy as np
# y=np.array([35,25,25,15])
# plt.pie(y)
# plt.show()

# Adding labels
# y=np.array([35,25,25,15])
# mylabels=["Apple","Banana","Cherry","Dates"]
# plt.pie(y,labels=mylabels)
# plt.show()

# start angle
# y=np.array([35,25,25,15])
# mylabels=["Apple","Banana","Cherry","Dates"]
# plt.pie(y,labels=mylabels,startangle=90)
# plt.show()


# explode
# y=np.array([35,25,25,15])
# myexplode=[0.2,0,0,0]
# mylabels=["Apple","Banana","Cherry","Dates"]
# plt.pie(y,labels=mylabels,startangle=90,explode=myexplode)
# plt.show()

# shadow
# y=np.array([35,25,25,15])
# mylabels=["Apple","Banana","Cherry","Dates"]
# plt.pie(y,labels=mylabels,startangle=90,shadow=True)
# plt.show()

# legend
y=np.array([35,25,25,15])
mylabels=["Apple","Banana","Cherry","Dates"]
plt.pie(y,labels=mylabels,startangle=90)
plt.legend()
plt.show()

# legend with title
y=np.array([35,25,25,15])
mylabels=["Apple","Banana","Cherry","Dates"]
plt.pie(y,labels=mylabels,startangle=90)
plt.legend(title="Four fruits:")
plt.show()

