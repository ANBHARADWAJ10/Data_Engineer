# find the largest value in a list

data = [10, 80, 30, 40, 50, 60, 100, 20, 90, 70]

# largest_value = -1

# for value in data:
#     if value > largest_value:
#         largest_value = value
    
# print("Largest value in the list is:", largest_value)

sum = 0

for value in data:
    sum += value
    print(sum, value)
