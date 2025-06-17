# set is a collection of unique elements
# # Sets are unordered collections of unique elements.
# Sets are defined by having values between curly braces {} or by using the set() constructor.
# Sets are mutable, meaning that you can add or remove items after the set has been created
# Sets cannout update or change the value of an existing item.
# Sets can be used to perform mathematical operations like union, intersection, and difference.
# Sets can contain items of different data types, but all items must be hashable.


set_data = {1, 2, 4, 3, 5}
print("set_data:", set_data)

# adding an item to a set
set_data.add(8)
print("data after adding an item:" , set_data)

# removing an item from a set
set_data.remove(2)
print("data after removing an item:", set_data)

# checking if an item is in a set
if 3 in set_data:
    print("3 is in the set")

# adding multiple items to a set using split() and update() operations
# only works with strings
# split() splits a string into a list of items based on the specified separator (default is
# user_input = input("Enter the multiple items using space\n")
# set_data.update(user_input.split())
# print("data after adding multiple items:", set_data)


#addding multiple items using loop()

count = int(input("enter the range\n"))

for i in range(count):
    item = int(input("Enter the item to add\n"))
    set_data.add(item)
print("data after adding multiple items using loop:", set_data)


# Union of two sets
# union basically combines two sets and returns a new set with all unique elements from both sets.

s1 = {1,2,4}
s2 = {3,4,5}
s3 = s1.union(s2)
print("Union of s1 and s2", s3)

# another way to perform union is using | pipe operator
s4 = s1 | s2
print("union using pipe operator:", s4)

# Intersection of two sets
# Intersection returns a new set with elements that are common to both sets.

ss1 = {1, 4, 5, 2, 3}
ss2 = {4, 5, 6, 7}

ss3 = ss1.intersection(ss2)
print("intersection of ss1 and ss2", ss3)

# another way to perform intersection us using & ampersand operator
ss4 = ss1 & ss2
print("intersection using ampersand operator:", ss4)