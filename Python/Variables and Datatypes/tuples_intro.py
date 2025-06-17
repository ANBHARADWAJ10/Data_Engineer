# tuple are immutable, order is preserved, can be used as dictionary keys, can contain mixed data types, and can be nested.
# Tuples are immutable sequences, typically used to store collections of heterogeneous items.
# Tuples are defined by having values between parentheses ().
# Tuples can contain items of different data types, including other tuples.

tuple_data = (1, 2, 3, 4, 5)
print("Tuple Data:", tuple_data)

tuple_data2 = ("apple", "banana", "cherry")

print(tuple_data2[0])

tuple_03 = (tuple_data, tuple_data2)

print("Nested Tuple:", tuple_03)

# Accessing elements in a tuple
print("first element of tuple_data:", tuple_data[0])

# Accessing a range of elements using slicing
print("range of 3 in tuple_data:", tuple_data[:3])

print(tuple_data2[1][3])

# Slicing a tuple
sliced_tuple = tuple_data[:3]
print("sliced tuple:", sliced_tuple)

# delete a tuple

# del tuple_data2
# print(tuple_data2)

# reverse a tuple

reversed_tuple = tuple_data[::-1]
print("reversed tuple:", reversed_tuple)

reversed_tup = tuple_data[::-2]
print("reversed tuple with step 2:", reversed_tup)