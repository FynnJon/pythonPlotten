import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from numpy.ma import indices
from scipy.stats import linregress

mpl.use('TkAgg')

data1 = pd.read_csv('a12_2.csv', sep='	')
data2 = pd.read_csv('a12_2b.csv', sep='	')
x1 = data1['anzahl1']
x2 = data2['anzahl1']
xs1 = np.std(x1)
xs2 = np.std(x2)
xm1 = np.mean(x1)
xm2 = np.mean(x2)
x = np.arange(0, 35, 0.1)

print(xs1)
print(xm1)
print(xs2)
print(xm2)

plt.hist(x1, bins=9, density=True, edgecolor='white')
plt.hist(x2, bins=24, density=True, edgecolor='white')
plt.plot(x, np.exp(-xm1)*((xm1**x)/sp.special.factorial(x)), '--', color='blue', label=r'Poisson-Verteilung: $\barx=2.31$, $\sigma=1.55$')
plt.plot(x, 1/(np.sqrt(2*np.pi)*xs2)*np.exp(-((x-xm2)**2)/(2*xs2**2)), '--', color='red', label=r'Gauß-Verteilung: $\barx=15.94$, $\sigma=3.92$')


plt.xlabel(r'Zählrate in Bq')
plt.ylabel(r'Relative Häufigkeit')
plt.axis([0, 30, 0, 0.31])
plt.legend()

plt.show()
