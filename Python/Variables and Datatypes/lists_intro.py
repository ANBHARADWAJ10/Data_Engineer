# Lists are mutable sequences, typically used to store collections of heterogeneous items.
# Lists are defined by having values between square brackets [].
# Lists can contain items of different data types, including other lists.
# Lists are ordered, meaning that the items have a defined order, and that order will not change unless you explicitly reorder the list.
# Lists are mutable, meaning that you can change, add, or remove items after the list has been created.
# Lists can be nested, meaning that you can have lists within lists.
# Lists can be sliced, meaning that you can access a subset of the list by specifying a range of indices.
# Lists can be iterated over, meaning that you can loop through the items in the list.
# Lists can be concatenated, meaning that you can combine two or more lists into a single list.
# Lists can be repeated, meaning that you can create a new list by repeating the items in an existing list.

data = [1, 2, 3, 4, 5]  # A simple list of integers
print("Data:", data)

# Accessing elements in a list
print("first element:", data[0])

# Slicing a list
print("first three elements:", data[:3])  # First three elements

data2 = data[:4]
print("data2:", data2)

# Modifying a list
data[0] = 10  # Change the first element
print("Modified data:", data)

# Adding elements to a list
data.append(6)  # Add an element to the end
print("Data after appending 6:", data)

# Inserting elements at a specific position
data.insert(0, 0)  # Insert 0 at the beginning 
print("Data after inserting 0 at the beginning:", data)

# Removing elements from a list
data.remove(3)  # Remove the first occurrence of 3
print("Data after removing 3:", data)

# Popping elements from a list
popped_element = data.pop()  # Remove and return the last element
print("Popped element:", popped_element)
print("Data after popping the last element:", data)

# Checking if an element exists in a list
if 2 in data:
    print("2 is in the list")

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.
# remove(): Removes the first occurrence of a specified element.
# pop(): Removes and returns an element at a specific position (default is the last element).
# clear(): Removes all elements from the list.
# index(): Returns the index of the first occurrence of a specified element.
# count(): Returns the number of occurrences of a specified element.
# sort(): Sorts the list in ascending order.
# reverse(): Reverses the order of the elements in the list.
# copy(): Returns a shallow copy of the list.


#converting a list to a tuple
data_tuple = tuple(data)  # Convert list to tuple  
print("Data as tuple:", data_tuple)
