import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = plt.subplot(111,projection='3d')

x= np.array([1])
y=np.array([1])
z=np.array([1])

ax1.scatter(x,y,z)
plt.show()

