import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

ax = plt.axes()

x = np.arange(1, 2.1, 0.1)
a1 = (2/x)+0.5
a2 = a1-1

plt.plot(x, a1, color='blue', label=r'Isotherme Expansion bei Temperatur $T_k$')
plt.plot(x, a2, color='red', label=r'Isotherme Kompression bei Temperatur $T_h$')
plt.vlines(1, 1.5, 2.5, color='black')
plt.vlines(2, 0.5, 1.5, color='black')

plt.text(0.95, 2.55, '1')
plt.text(0.95, 1.45, '4')
plt.text(2.05, 1.55, '2')
plt.text(2.05, 0.45, '3')
ax.set_xticks([1, 2])
ax.set_xticklabels(['$V_{UT}$', '$V_{OT}$'])
plt.text(1.5, 1.3, '$W$')

plt.tick_params(axis='y', which='both', left=False, labelleft=False)

plt.xlabel(r'$V$')
plt.ylabel(r'$p$')

plt.axis([0.5, 2.5, 0, 3.2])
plt.legend()
plt.show()
