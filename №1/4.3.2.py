import numpy as np
import matplotlib.pyplot as plt
import math as m
# x = int(input("Введи"))
q = []
for x in (range(1, 11)):
    q.append((m.sqrt(1 + m.e**(m.sqrt(x)) + m.cos(x)**2) / (abs(1 - m.sin(x)**3))))
print(q)
a = q[1:6:]
plt.scatter(range(len(a)), a, color = 'blue', marker='o')
plt.plot(range(len(q)), q, color = 'r', linestyle = '-')
plt.grid(True)
plt.show()
