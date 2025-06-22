import numpy as np

# matmul function for multiplying two arrays.
a = np.ones((2,3))
b = np.full((3,2),2)

print(a)
print(b)
result = np.matmul(a,b)
print(result)

# To find the determinent of a square matrix (works only if there are same rows and columns)

c = np.identity(3)
print(c)
determinent = np.linalg.det(c)
print(determinent)



# Reference = https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

# Determinent
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse etc..