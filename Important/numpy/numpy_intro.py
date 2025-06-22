import numpy as np

# one dimensional Array
a = np.array([1,2,3,4,5,6])
print(a)
print(a.ndim)
print(a.shape)

# two dimensional Array
b = np.array(
    [[1,2,3],
     [4,5,6]]
)
print(b)
print(b.ndim)
print(b.shape)

# 3d array

c = np.array(
    [
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
    ]
)
print(c)
print(c.ndim)
print(c.shape)

# print only ones
# a = empty(shape, dtype, order, device=device)
# one = np.ones((2,3,4)) this one works as well.
one = np.ones(shape = (2,3,4), dtype = 'int16')
print(one)
print(one.dtype)

# print only zeroes
zero = np.zeros(shape = (2,3))
print(zero)

# identity matrix
identity_matrix = np.identity(3)
print(identity_matrix)

# random matrix 
random_matrix = np.random.randint(3,7,size = (2,3,3))
print(random_matrix)

# works when working on at least a 2d.

rand = np.array([[1,2,3]])
repeated_matrix = np.repeat(rand, 3, axis = 0)
print(repeated_matrix)
print(rand.ndim)

# full array

full_array = np.full((3,2), 2) # 3 rows and 2 columns and all filled with the number 2.
print(full_array)