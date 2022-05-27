import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('e7_1.csv', sep=';')

x = np.arange(0.0, 3.0, 0.01)

y1 = x
y2 = x/(((x*(1-x))/5)+1)
y3 = x/(((x*(1-x))/0.5)+1)
y4 = x/(((x*(1-x))/0.05)+1)

a = y3 > 0
b = y4 > 0

plt.plot(x, y1, color='red')
plt.plot(x, y2, color='blue')
plt.plot(x[a], y3[a], color='orange')
plt.plot(x[b], y4[b], color='green')
plt.axis([0, 1, 0, 1])
plt.grid()
plt.xlabel(r"$\frac{R_{AC}}{R_{AB}}$")
plt.ylabel(r"$\frac{U_L}{U_0}$", rotation=0)

plt.show()
