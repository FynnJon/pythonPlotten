import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('Radonzerfall.csv', sep='	')

x_data = data['zeitinmin']
y_data = data['rate']
x_err = 0
y_err = 0.10544
x = np.arange(0, 200, 1)

#plt.scatter(x_data, y_data)
plt.errorbar(x_data, y_data, y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
#plt.plot(x_data, np.exp(lin.intercept)*np.exp(lin.slope*x_data), label=r'$7.954e^{-0.688d}$')
plt.plot(x, 0*x+0.5064)

plt.grid()
plt.axis([0, 185, 0, 12])
plt.xlabel(r'Zeit in min')
plt.ylabel(r'Zählrate $Z$ in 1/s')
#plt.legend()

plt.show()
