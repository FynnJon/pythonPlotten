import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('a12_4.csv', sep=';')

x_data = data['dichte_ker']
y_data = data['rate_korr']
x_err = 0
y_err = data['rate_err']

plt.errorbar(x_data, y_data, y_err, fmt='x', linewidth=0.8, capsize=1.5)

#plt.axis([0, 0.8, 0, 4])
plt.xlabel(r'Kehrwert der Dichte in cm$^3$/g')
plt.ylabel(r'Zählrate in Bq')

plt.show()
