import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('a12_5.csv', sep=';')

x_data = data['1/r^2']
y_data = data['rate_korr']
x_err = data['r_k_err']
y_err = data['rate_err']

lin = linregress(x_data, y_data)
print(lin)
x = np.arange(0, 0.1, 0.1)

plt.errorbar(x_data, y_data, y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
plt.plot(x_data, lin.slope*x_data+lin.intercept, label=r'y=254.88x-1.32')

#plt.grid()
plt.axis([0, 0.03, 0, 6.1])
plt.xlabel(r'$1/r^2$ in 1/cm$^2$')
plt.ylabel(r'Zählrate $Z$ in Bq')
plt.legend()

plt.show()
