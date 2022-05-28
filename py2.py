import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('e7_2d.csv', sep=';')

x_data = data['R_AC/R_AB']
x_err = data['poti err']
y1_data = data['U_L/U_0(1)']
y2_data = data['u/u(2)']
y3_data = data['u/u(3)']
y4_data = data['u/u(4)']
y1_err = data['u/u err(1)']
y2_err = data['u/u err(2)']
y3_err = data['u/u err(3)']
y4_err = data['u/u err(4)']

x = np.arange(0.0, 1.0, 0.01)
y1 = x
y2 = x/(((x*(1-x))/5)+1)
y3 = x/(((x*(1-x))/0.5)+1)
y4 = x/(((x*(1-x))/0.05)+1)

a = y3 > 0
b = y4 > 0

plt.plot(x, y1, color='red', linewidth=0.7)
plt.errorbar(x_data, y1_data, y1_err, x_err, fmt=',', linewidth=0.7, capsize=2, color='red')
plt.plot(x, y2, color='blue', linewidth=0.7)
plt.errorbar(x_data, y2_data, y2_err, x_err, fmt=',', linewidth=0.7, capsize=2, color='blue')
plt.plot(x[a], y3[a], color='orange', linewidth=0.7)
plt.errorbar(x_data, y3_data, y3_err, x_err, fmt=',', linewidth=0.7, capsize=2, color='orange')
plt.plot(x[b], y4[b], color='green', linewidth=0.7)
plt.errorbar(x_data, y4_data, y4_err, x_err, fmt=',', linewidth=0.7, capsize=2, color='green')
plt.axis([0, 1, 0, 1])
plt.grid()
plt.xlabel(r"$\frac{R_{AC}}{R_{AB}}$")
plt.ylabel(r"$\frac{U_L}{U_0}$", rotation=0)

plt.show()
