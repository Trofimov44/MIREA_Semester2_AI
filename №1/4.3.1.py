import numpy as np
import matplotlib.pyplot as plt
n = 10
array = np.random.rand(n)
b = np.mean(array)
c = np.median(array)

print("Среднее значение: ", b)
print("Медианное значение: ", c)

if b > c:
    print("Среднее значение больше медианного значения.")
elif b < c:
    print("Медианное значение больше среднего значения.")
else:
    print("Среднее и медианное значения равны.")
plt.scatter(range(len(array)), array, marker='o', color='b',)
plt.grid(True)
plt.show()
