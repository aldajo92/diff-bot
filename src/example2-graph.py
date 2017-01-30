# This script shows how to plot data
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


time1 = np.arange(0., 5., 0.2)
time2 = np.arange(0., 5., 0.02)

position1 = f(time1)
position2 = f(time2)

plt.plot(time1, position1, 'bo', time2, position2, 'k')
plt.show()
