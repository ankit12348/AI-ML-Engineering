import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print(numbers)

mat = np.array([[1, 2], [3, 4]])

print(mat)
print(mat.shape)
print(mat.ndim)

arr = np.array([1, 2, 3, 4, 5])
print(arr[:3])
print(arr[-2:])

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a * b)