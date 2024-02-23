import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Создание словаря
data = {
    'Apple': [132.69, 134.14, 121.26, 134.87, 125.35, 136.69, 145.11, 148.99, 148.56, 156.69, 172.29, 181.68],
    'Microsoft': [222.42, 242.82, 232.33, 249.72, 245.79, 259.43, 267.57, 286.54, 299.25, 332.75, 338.91, 321.89],
    'Google': [1824.97, 1921.35, 2050.00, 2060.12, 2337.02, 2451.76, 2713.83, 2825.45, 2821.99, 2957.62, 2823.05, 2894.08]
}

plt.grid(True)
plt.plot(data['Apple'], color = 'g', marker='o')
plt.plot(data['Microsoft'], color = 'b', marker='o')
plt.plot(data['Google'], color = 'r', marker='o')
plt.show()

# a = yf.download('AAPL', '2021-01-01', '2021-12-31')
# b = yf.download('MSFT','2021-01-01', '2021-12-31')
# d = yf.download('GOOG', '2021-01-01', '2021-12-31')
# 
# plt.grid(True)
# plt.plot(a, color = 'g')
# plt.plot(b, color = 'b')
# plt.plot(d, color = 'r')
# plt.show()
