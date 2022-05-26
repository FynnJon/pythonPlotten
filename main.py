from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

data = pd.read_csv('e7_1.csv', sep=';')

x_data = data['I in mA']
y_data = data['U in V']
x_err = data['I error']
y_err = data['U error']

plt.errorbar(x_data, y_data, y_err, x_err, fmt=',', linewidth=1, capsize=2)

plt.show()
