# Extract the last and first element from the list
L1 = [10, 20, 30, 40, 50, 60]

print('last-element:', L1[-1])
print('first-element:', L1[0])

# Extract the following list from L1 defined above by use of slicing.
# [20, 30, 40]

extracted_list = L1[1:4]
print(extracted_list)

# Remove the duplicates from the following list:

L2 = ['Hi', 'Hello', 'Hi!', 'Hey', 'Hi', 'hey', 'Hey']

rm_duplicates = set(L2)
print(rm_duplicates)

# Given the dictionary
# Play around with extracting the values by calling out the keys for all key/value pairs

d = {2: 122, 3: 535, 't': 'T', 'rum': 'cola'}

print(d[2])
print(d['rum'])

# create a for loop that prints:
# '23 sqaured is 529'
# '73 sqaured is 5329'
# '12 sqaured is 144'
# '84 sqaured is 7056'
n = [23, 73, 12, 84]

squares = [num ** 2 for num in n]

for i,j in zip(n,squares):
    print(f'{i} squared is {j}')

# Use a list comprehension to create a new list with areas of the circles that have diameters defined by
import math
diameters = [10, 12, 16, 20, 25, 32]

areaOfCircle = [3.14 * (d/2)**2 for d in diameters]
print(areaOfCircle)
# convert elements to string and round down
print([f'{area:.0f}' for area in areaOfCircle])


# From the following list, create a new list containing only the elements that have exactly five characters.

phonetic_alphabet = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']

five_char = [i for i in phonetic_alphabet if len(i) == 5]

print(five_char)

# Find the intersection of the two sets (elements that occur in both sets)

s1 = {'HE170B', 'HE210B', 'HE190A', 'HE200A', 'HE210A', 'HE210A'}

s2 = {'HE200A', 'HE210A', 'HE240A', 'HE200A', 'HE210B', 'HE340A'}

s3 = s1.intersection(s2)

print(s3)

# Create a variable fy and set it equal to 435.

# Given the tuple below, create a list where each value is:

# The value itself if the value is below fy
# fy if the value is larger than fy

rebar_stresses = (125, 501, 362, 156, 80, 475, 489)

fy = 435

result = [i if i < fy else fy for i in rebar_stresses]

print(result)

# Given the tuple below, create a list where each value is:

# 0 if the value is positive
# The value itself is the value is negative and larger than -25
# -25 if the value is lower than -25
T1 = (-18, -27, 2, -21, -15, 5)

negative_list = [0 if i > 0 else i for i in T1]
print(negative_list)