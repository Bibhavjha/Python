import numpy as np
arr=np.array([11,21,34,4,15])
i=np.where(arr==21)
print(i)
j=np.where(arr>12)
print(j)

import numpy as np
arr=np.array([11.,21,34,44,55])
values=[25,46]
i=np.searchsorted(arr,values)
print(i)

import numpy as np
arr=np.array([11,21,34,55,44])
print(np.any(arr>40))
print(np.all(arr>15))