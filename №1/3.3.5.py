x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = x[1::2]
b = x[0::2]
b = b[::-1]
q = []
# print(a)
# print(b)
# if len(b) > len(a):
#     c = len(b)
# else:
#     c = len(a)
for i in range(0, len(a)):
    q.append(b[i])
    q.append(a[i])
print(q)
