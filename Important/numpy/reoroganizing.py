import numpy as np

# Reorganizing the array

before = np.array(
    [[1,2,3,4],[5,6,7,8]]
)

print(before)

after = before.reshape(4,2)
print(after)

# vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

stack = np.vstack([v1,v2])
print(stack)

# horizontal stack the rows should match

h1 = np.ones((3,3))
h2 = np.full((3,6),2)
stack_hor = np.hstack((h1,h2))
print(stack_hor)


# Local data from a file

# filedata = np.genfromtxt('data.txt', delimeter = ',')
# filedata.astype('int32')

# Boolean masking and advanced indexing

print(h1 > 50) # prints the boolean value as true if the expression is true. vice versa
print(h1[h1 > 0])

# print the values with the help of indexing 

h1[1,3] # mention the index and you get the value residing in the index.

# '~' - not 

