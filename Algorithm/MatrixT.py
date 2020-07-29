import numpy as np

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = np.array(a)
# for i in a:
#     i = i[::-1]
#     print(i)
a = a.T
print(a)
for i in range(len(a)):
    a[i] = a[i][::-1]
print(a)