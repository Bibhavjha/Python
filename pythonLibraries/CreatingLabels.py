import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=np.array([240,250,200,270,280,290,300,100,200,200,400,230])
plt.plot(x,y)
# plt.title('monthly Expenditure')
# plt.xlabel("months")
# plt.ylabel("Expenses in s")
# plt.show()
# set font 
f1={'family':'serif','color':'blue','size':20}
f2={'family':'serif','color':'darkred','size':15}
# plt.title('monthly Expenditure',fontdict=f1)
# plt.xlabel("months",fontdict=f2)
# plt.ylabel("Expenses in s",fontdict=f2)
# plt.show()

# position for title
# plt.title('monthly Expenditure',loc='left')
# plt.show()

# to display grid lines:-
# plt.xlabel("months",fontdict=f2)
# plt.ylabel("Expenses in s",fontdict=f2)
# plt.grid()
# plt.show()

# To specify grid lines
# plt.xlabel("months",fontdict=f2)
# plt.ylabel("Expenses in s",fontdict=f2)
# plt.grid(axis='x')
# plt.show()

# to change grid color and style
plt.xlabel("months",fontdict=f2)
plt.ylabel("Expenses in s",fontdict=f2)
plt.grid(axis='x',color="green",ls='--',lw=2.5)
plt.show()


