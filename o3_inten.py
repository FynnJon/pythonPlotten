import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import linregress

mpl.use('TkAgg')

a = 0.000001
x = np.arange(-a, a, a/100)

#einzel
phi1 = (3.141*1*np.sin(x)/(500*(10**(-9))))
FES = ((np.sin(phi1) * np.sin(phi1)) / (phi1 ** 2))
#doppel
phi2 = (3.141*3*np.sin(x)/(500*(10**(-9))))
FP = (np.sin(2*phi2) * np.sin(2*phi2)) / (np.sin(phi2) * np.sin(phi2))
#gitter
phi3 = (3.141*3*np.sin(x)/(500*(10**(-9))))
FP2 = (np.sin(10*phi3) * np.sin(10*phi3)) / (np.sin(phi3) * np.sin(phi3))


einzel = FES
doppel = FP*FES
gitter = FES*FP2


fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
#, sharex=True, figsize=(12, 6)

fig.canvas.draw()
labels = [item.get_text() for item in ax0.get_xticklabels()]
labels[1] = 'Testing'

ax0.plot(x, einzel, linewidth=0.8)
ax1.plot(x, doppel, linewidth=0.8)
ax1.plot(x, einzel*4, linewidth=0.8, linestyle='--')
ax2.plot(x, gitter, linewidth=0.8)
ax2.plot(x, einzel*100, linewidth=0.8, linestyle='--')

ax0.tick_params(axis='both', which='both', left=False, labelleft=False, bottom=False, labelbottom=False)
ax1.tick_params(axis='both', which='both', left=False, labelleft=False, bottom=False, labelbottom=False)
ax2.tick_params(axis='both', which='both', left=False, labelleft=False, bottom=False, labelbottom=False)

ax0.set_xlabel('Beugungswinkel')
ax0.set_ylabel('Intensität')
ax1.set_xlabel('Beugungswinkel')
ax1.set_ylabel('Intensität')
ax2.set_xlabel('Beugungswinkel')
ax2.set_ylabel('Intensität')

ax0.set_title('Einzelspalt')
ax1.set_title('Doppelspalt')
ax2.set_title('Gitter')

plt.show()
