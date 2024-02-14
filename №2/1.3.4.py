from numpy import *
b = 10
c = b - 1
x = array([zeros(b)]*b)

for i in range(b):
    x[c, i] = 1
c -= (b - 1)
for i in range(b):
    x[c, i] = 1
for i in range(b):
    x[c, (b-1)] = 1
    x[c, 0] = 1
    c += 1
print(x)
