import copy

# Shallow copy vs Deep copy

# Shallow copy creates a new object, but inserts references into it to the objects found in the original.
original_list = [1, 2, 3, [4,5]]

shallow_copied_list = copy.copy(original_list)

deep_copied_list = copy.deepcopy(original_list)

shallow_copied_list[3][1] = 10

deep_copied_list[3][0] = 20


print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)
