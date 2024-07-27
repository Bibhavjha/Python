import numpy as np
arr=np.array([5,10,15])
for index, x in np.ndenumerate(arr):
    print(index,x)