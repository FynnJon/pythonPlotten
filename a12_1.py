import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data1 = pd.read_csv('Radonzerfall.csv', sep='	')
data2 = pd.read_csv('Radonzerfall2.csv', sep='	')

x_data = data2['zeitinmin']
y_data = data2['rate']
x_nr = data1['zeitinmin']
y_nr = data1['rate']
nullrate = np.mean(y_nr)
err = np.std(y_nr)
print(nullrate)
print(err)
x_err = 0
y_err = 2*err
x = np.arange(0, 200, 1)

plt.errorbar(x_data, y_data, y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
plt.errorbar(x_nr, y_nr, y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
#plt.plot(x_data, np.exp(lin.intercept)*np.exp(lin.slope*x_data), label=r'$7.954e^{-0.688d}$')
plt.plot(x, 0*x+nullrate)

plt.grid()
plt.axis([0, 185, 0, 12])
plt.xlabel(r'Zeit in min')
plt.ylabel(r'Zählrate $Z$ in Bq')
#plt.legend()

plt.show()
