import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('a12_5.csv', sep=';')

x_data = data['d in cm']
y_data = data['rate_korr']
x_err = data['d_err']
y_err = data['rate_err']

lin = linregress(x_data, np.sqrt(1/y_data))
print(lin)
x = np.arange(0, 14, 0.1)

plt.errorbar(x_data, np.sqrt(1/y_data), y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
plt.plot(x, (lin.intercept)^2*x)

plt.grid()
#plt.axis([0, 5, 0, 10])
plt.xlabel(r'Abstand $d$ in cm')
plt.ylabel(r'Zählrate $Z$ in 1/s')
plt.legend()

plt.show()
