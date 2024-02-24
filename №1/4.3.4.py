import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

a = yf.download('AAPL', '2021-01-01', '2021-12-31')
b = yf.download('MSFT','2021-01-01', '2021-12-31')
d = yf.download('GOOG', '2021-01-01', '2021-12-31')

plt.grid(True)
plt.plot(a, color = 'g')
plt.plot(b, color = 'b')
plt.plot(d, color = 'r')
plt.show()
