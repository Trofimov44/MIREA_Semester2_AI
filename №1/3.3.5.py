x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = x[1::2]
b = x[0::2]
b = b[::-1]
q = []
for i in range(0, c):
    q.append(b[i])
    q.append(a[i])
print(q)
