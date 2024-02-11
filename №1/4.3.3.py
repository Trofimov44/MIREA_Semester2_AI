from scipy.integrate import simps
from numpy import trapz
import numpy as np
import matplotlib.pyplot as plt
import math as m


x = np.arange(0.0,10,1)
y = np.abs(np.cos(x*np.e**(np.cos(x)+np.log(x+1))))

plt.grid(True)
plt.plot(x,y, color = 'r')
plt.fill_between(x,y)
a = trapz(y)
print(a)
plt.show()
