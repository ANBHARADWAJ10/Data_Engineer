import math
import timeit
# # list
# mylist = [1,2,3,4,5]
# print(mylist)
#
# #slicing
# a = mylist[::-1]
# print(a)
#
#
# list_org = ['banana', 'mango', 'apple']
# lsit_cpy = list_org.copy()
# list_02 = list(list_org)
#
# a = [1,2,3,4,5]
# b = [int(math.pow(i,3)) for i in a]
# print(a)
# print(b)

# Tuple
# mytuple = ('nikhil', 'spiderman', 'avengers', 'ironman', 'ironman')
# # print(type(mytuple))
# # print(mytuple)
# # print(mytuple[0:2])
# mytuple_02 = tuple(['nikhil', 'spiderman', 'avengers', 'ironman'])
# print(mytuple_02)
#
# # print(mytuple.count('ironman'))
#
# # print(len(mytuple))
#
# print(timeit.timeit(stmt='[1,2,4,5,6]', number=1000))
#
# mydict = {'Germany': 'Bmw', 'India':'Tata', 'Usa':'Tesla'}
# print(mydict.values())
# print(mydict.keys())
# print(mydict['Germany'])
# print(mydict.get('India'))
# mydict.pop('Germany')
# print(mydict)
# mydict.update({'Germany': 'Porsche'})
# print(mydict)
# for i in mydict.values():
#     print(i)
#
# for cars in mydict.keys():
#     print(f'country: {cars}, cars: {mydict[cars]} ')
#
# for key, value in mydict.items():
#     print(f'{key}: {value}')

# set
# myset = {'1','2','3','4','5','6','7','8','9'}
# print("myset:", myset)
#
# myset_02 = {'2','3','4','5','6','7'}
#
# print(myset.union(myset_02))
# print(myset.intersection(myset_02))
# print(myset.difference(myset_02))
# print(myset.symmetric_difference(myset_02))
# print(myset.issubset(myset_02))
#
# a = frozenset({1, 2, 3, 4})
# print(a)

# string

# mystring = 'nikhil'
# print(type(mystring))
# print(mystring)
# print('I\'m nikhil')
# print("I'm Nikhil")
# print(''' used for multiline string
# super man''')

# mystring = 'Hello World   '
# char = mystring[0]
# print(char)
# print(mystring[1:3])
# new_stirng = mystring.strip()
# print(new_stirng)
# print(mystring.upper())
# print(mystring.lower())
# print(mystring.startswith('Hello'))
# print(mystring.endswith('World'))
# print(mystring.count('i'))
# print(mystring.find('o'))
# print(mystring.replace('i', 'o'))
# mylist = mystring.split()
# print(mylist)
# new_string = ''.join(mylist)
# print(new_string)
# str = 'Tom'
# n_str = 'Hey this is my fav character %s' %str
# print(n_str)
# num = 10
# d_str = 'Hey this is my lucky %d' %num
# print(d_str)







