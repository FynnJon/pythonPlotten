import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data1 = pd.read_csv('a12_2.csv', sep='	')
data2 = pd.read_csv('a12_2b.csv', sep='	')
x1 = data1['anzahl1']
x2 = data2['anzahl1']

plt.hist(x1, bins=9, edgecolor='white')
plt.hist(x2, bins=24, edgecolor='white')

plt.xlabel(r'Zählrate in 1/s')
plt.ylabel(r'Häufigkeit')
plt.axis([0, 30, 0, 140])

plt.show()
