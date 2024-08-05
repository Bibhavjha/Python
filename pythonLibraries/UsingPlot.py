import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,45])
ypoints=np.array([5,55])
plt.plot(xpoints,ypoints)
plt.show()
plt.plot(xpoints,ypoints,'o')
plt.show()
plt.plot(xpoints,ypoints,marker='o')
plt.show()
