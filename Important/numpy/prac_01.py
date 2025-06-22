import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

print(np.zeros((3,3)))

print(np.ones((3,3)))

print(np.arange(0, 10, 2))

print(np.random.randint(5, 7, (3,3,3)))
# size = (depth, rows, columns)

# identity matrix
print(np.eye(4))

print(np.full((3,3,3),7))

print(np.linspace(0,10,5))
