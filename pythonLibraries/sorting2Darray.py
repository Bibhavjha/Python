import numpy as np
arr=np.array([[3,5,2],[8,4,6]])
arr1=np.sort(arr)
print(arr1)
arr2=np.sort(arr,axis=0)
print(arr2)
arr3=np.argsort(arr)
print(arr3)