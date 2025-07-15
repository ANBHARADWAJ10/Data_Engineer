from itertools import *

#product
a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=1)
print(list(prod))

# permutations

a_01 = [1, 2, 3]
perm = permutations(a_01, 2) # here the 2 is length
print(list(perm))

# combinations
a_02 = [1, 2, 3, 4]
comb = combinations(a_02, 2)
print(list(comb))

# combinations with replacing itself
comb_02 = combinations_with_replacement(a_02, 2)
print(list(comb_02))

# accumulate

acc = accumulate(a_02)
print(list(acc))

# # groupby
#
# gruop = groupby(a_02)
# print(list(gruop))
