import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
X, Y = np.mgrid[-1:1:30j, -1:1:30j]
Z = X**2+Y**2 + 1
ax.plot_surface(X, Y, Z, cmap="Greens_r", lw=0, rstride=2, cstride=2)
ax.contour(X, Y, Z, 10, lw=3, cmap="Greens_r", linestyles="solid", offset=1)
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
plt.show()
