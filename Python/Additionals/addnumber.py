def add_nums(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum



# for i in range(5):
#     values = add_nums(int(input()), int(input()))
#     print(values)

letters = ['a', 'b', 'c', 'd', 'c']

# enumerate is used to help us in finding the index and show us the value alongside it.

for idx, letter in enumerate(letters):
    print(idx, letter)

# we can achieve the same with just looping but it not recommended

for i in range(len(letters)):
    print(i, letters[i])

# Define a list of circle diameters
diameters = [10, 12, 16, 20, 25]                    

# Compute circle area by list comprehension
areas = [3.14 * (d/2)**2 for d in diameters]

# Print (diameter, area) pairs
for d, a in zip(diameters, areas):
    print(d, a)