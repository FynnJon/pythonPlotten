import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('a12_3.csv', sep=';')

x_data = data['d in mm']
y_data = data['rate_korr']
x_err = data['d_err']
y_err = data['rate_err']

#lin = linregress(x_data, np.log(y_data))
#print(lin)
A = 8.34729
l = 1/1.183561
offset = 0.3496887
x = np.arange(0, 6, 0.2)

plt.errorbar(x_data, y_data, y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
#plt.plot(x_data, np.exp(lin.intercept)*np.exp(lin.slope*x_data), label=r'$7.954e^{-0.688d}$')
plt.plot(x, offset+A*np.exp(-l*x), label=r'$8.35e^{-0.84d}+0.35$')

plt.grid()
plt.axis([0, 5, 0, 10])
plt.xlabel(r'Papierdicke $d$ in mm')
plt.ylabel(r'Zählrate in Bq')
plt.legend()

plt.show()
