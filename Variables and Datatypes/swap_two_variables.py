x = 2
y = 4
print(x, y)
# Swap the values of x and y most efficent method cause it does not use any extra memory

# Method 1: using tuple unpacking
x, y = y, x
print(x, y)

# Method 2: using a temporary variable
temp = x
x = y
y = temp
print(x, y)

#MEthod 3: using arithmetic operations
# This method works only for numeric types and can lead to overflow issues in some languages.
# It is not recommended for general use.
# It works only if y is not equal to 0, otherwise it will lead to an error.
# It takes extra memory for the variables
x = x + y
y = x - y
x = x - y
print(x, y)

# Method 4: using bitwise XOR
# This method works only for integer types and can lead to unexpected results if the values are not integers.
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)