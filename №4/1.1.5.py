import numpy as np
import scipy as sp
from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt

beta = (5, 2, 1)
def f(x,b0,b1,b2):
    return b0 + b1*x+b2*x*x

xdata = np.linspace(0,7,20)
y = f(xdata, *beta)

ydata = y + 0.05 * np.random.rand(len(xdata))
beta_opt, beta_cov = sp.optimize.curve_fit(f,xdata,ydata)
beta_opt

lin_dev = sum(beta_cov[0])
lin_dev

residuals = ydata -f(xdata, *beta_opt)
fres = sum(residuals**2)
fres

fig,ax = plt.subplots()
ax.scatter(xdata,ydata)
ax.plot(xdata,y,'r',lw =2 )
ax.plot(xdata,f(xdata,*beta_opt),'b',lw = 2)
ax.set_xlim(0,5)
ax.set_xlabel(r"$x$", fontsize = 18)
ax.set_ylabel(r"$f(x,\beta)$", fontsize = 18)
plt.show()
