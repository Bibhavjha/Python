import numpy as np
surname=('airee','kami','khadka')
firstname=('dipendra','sompal','paras')
ind=np.lexsort((surname,firstname))
print(ind)
arr=[ firstname[i]+" "+surname[i] for i in ind]
print(arr)