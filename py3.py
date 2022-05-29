import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data = pd.read_csv('e7_letzte.csv', sep=';')

x_data = data['R_AC/R_AB']
x_err = data['poti err']
#y1_data = data['U_L/U_0(1)']
y2_data = data['n(2)']
y3_data = data['n(3)']
y4_data = data['n(4)']
#y1_err = data['u/u err(1)']
y2_err = data['n(2)err']
y3_err = data['n(3)err']
y4_err = data['n(4)err']

#plt.errorbar(x_data, y1_data, y1_err, x_err, fmt=',', linewidth=0.7, capsize=2, color='red')
plt.errorbar(x_data, y2_data, y2_err, x_err, fmt=',', linewidth=1, capsize=2, color='blue')
plt.errorbar(x_data, y3_data, y3_err, x_err, fmt=',', linewidth=1, capsize=2, color='orange')
plt.errorbar(x_data, y4_data, y4_err, x_err, fmt=',', linewidth=1, capsize=2, color='green')
plt.axis([0, 1, 0, 1])
plt.grid()
plt.xlabel(r"$\frac{R_{AC}}{R_{AB}}$")
plt.ylabel(r"$\frac{P_L}{P_0}$", rotation=0)

plt.show()
