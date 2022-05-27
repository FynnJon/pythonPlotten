import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('e7_1.csv', sep=';')

#x_data = data['I in mA']
#y_data = data['U in V']
#x_err = data['I error']
#y_err = data['U error']

x_data = data['R in Ohm']
y_data = data['P in mW']
x_err = data['R error']
y_err = data['P err in mW']

#lin = linregress(x_data. y_data)
#print(lin)

plt.errorbar(x_data, y_data, y_err, x_err, fmt=',', linewidth=0.8, capsize=1.5)
#plt.plot(x_data. lin.intercept + lin.slope*x_data)

plt.grid()
plt.xlabel(r'Widerstand $R$ in $\Omega$')
plt.ylabel(r'Leistung $P$ in mW')

plt.show()
