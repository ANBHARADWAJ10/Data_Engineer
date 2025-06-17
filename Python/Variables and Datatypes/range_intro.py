# range is used to generate a series of numbers within a given range

# range(stop)
# range(start, stop)
# range(start, stop, step)

# if the user wants increment, then the user needs to use positive step
# if the user wants decrement, then the user needs to use negative step

# range(stop)

for i in range(10):
    print(i, end= " ")

print("\n")

# range(start, stop)
for i in range(5, 10):
    print(i, end=" ")

print("\n")

# range(start, stop, step)
# increment

for i in range(1, 10, 2):
    print(i, end=" ")

print("\n")

# decrement
for i in range(10, 0, -1):
    print(i, end=" ")
