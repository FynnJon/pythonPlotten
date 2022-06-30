import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

fig, axs = plt.subplots(nrows=1, ncols=1)


x = np.arange(-1.5, 1.5, 0.01)
varphi=(3.141*0.000001*np.sin(x)/(500*(10**(-9))))
FES=((np.sin(varphi) * np.sin(varphi)) / (varphi ** 2))

axs[0, 0].plot(x, FES)

plt.show()
