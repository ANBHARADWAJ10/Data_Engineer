# id() is a built-in function in Python that returns the identity of an object.
# The identity of an object is a unique integer that represents the object's memory address.
# The id() function is useful for checking if two variables point to the same object in memory.
# It can also be used to check if a variable is None or not.

a = 10
b = a
c = 20
print("ID of a:", id(a))  # ID of a
print("ID of b:", id(b))  # ID of b (should be same as a)
print("ID of c:", id(c))  # ID of c (should be different from a and b)
print("Are a and b the same object?", a is b)  # True, since b points to the same object as a

#type() is a built-in function in Python that returns the type of an object.
#int
print("type of a:", type(a))

#string
name = "Nikhil Bharadwaj"
print("type of name:", type(name))  # Should return <class 'str'>

#float
height = 5.7
print("type of height:", type(height))  # Should return <class 'float'>