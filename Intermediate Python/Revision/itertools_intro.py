# itertools: product, permutations, combinations, groupby and infinite iterators

# tools used in for loop

# from itertools import product
#
# a = [1,2]
# # b = [3,4]
# b = [3]
# prod = product(a,b, repeat=2)
# print(list(prod))
#
# from itertools import permutations
#
# a = [1,2,3]
# perm = permutations(a)
# print(list(perm))

# from itertools import combinations
# a = [1,2,3,4]
# comb = combinations(a,2)
# print(list(comb))

#accumulate

# from itertools import accumulate
# # returns accumulated sum
#
# a = [1,2,3,4]
# acc = accumulate(a)
# print(list(acc))
#
# import operator
# b = [1,2,3,4,5]
# acc2 = accumulate(b, func=operator.mul )
# print(list(acc2))

# groupby
# from itertools import groupby
# a = [1,2,3,4]
# group_obj = groupby(a, key=lambda x: x < 3)
# for k,v in group_obj:
#     print(k, list(v))

#infinite loop
# from itertools import count, cycle, repeat
#
# # for i in count(1):
# #     if i == 100:
# #         break
# #     print(i)
# #
# # a = [1,2,3]
# # for i in cycle(a):
# #     print(i)
#
# for i in repeat(1,3):
#     print(i)