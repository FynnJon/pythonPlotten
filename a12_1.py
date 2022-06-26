import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

data1 = pd.read_csv('Radonzerfall.csv', sep='	')
data2 = pd.read_csv('Radonzerfall2.csv', sep='	')

x_data = data2['zeitinmin']
y_data = data2['rate']
x_nr = data1['zeitinmin']
y_nr = data1['rate']
nullrate = np.mean(y_nr)
err = np.std(y_nr)
print(nullrate)
print(err)
#x_err = x_data*0.02
y_err = 2*err
x = np.arange(0, 200, 1)
y1 = 11.94*np.exp(-0.0122*(x-30.0483))-1.06+nullrate
y2 = 0.5*np.exp(-0.001155*(x-30.0483))+nullrate
y3 = y1-y2

#Nullrate
plt.errorbar(x_nr, y_nr, y_err, x_nr*0.02, fmt=',', linewidth=0.7, capsize=0.9, color='green')
plt.plot(x, 0*x+nullrate, color='green', linewidth=0.7, label='Nullrate')
#Messdaten
plt.errorbar(x_data, y_data, y_err, x_data*0.02, fmt=',', linewidth=0.7, capsize=0.9, color='blue', label='Zerfallsmessung')
plt.plot(x, y1, color='blue', linewidth=0.7, label=r'$f(t)=11.94e^{-0.012t}-1.06$')
#plt.plot(x, y2)
plt.plot(x, y3, color='orange', linewidth=0.7, label=r'$g(t)=f(t)-0.5e^{-0.001155t}$')
plt.vlines(30.0483, 5.19, 10.38, linewidth=0.7, color='red')
plt.text(27.5, 7.785, r'$Z_0-Z_{1/2}$', rotation='vertical', va='center', ha='center', color='red')
plt.hlines(5.19, 30.0483, 46.958+30.0483, linewidth=0.7, color='red')
plt.text(53.53, 4.8, r'$T_{1/2}-T_0$', va='center', ha='center', color='red')

#plt.grid()
plt.axis([0, 185, 0, 12])
plt.xlabel(r'Zeit $t$ in min')
plt.ylabel(r'Zählrate $Z$ in Bq')
plt.legend()

plt.show()
