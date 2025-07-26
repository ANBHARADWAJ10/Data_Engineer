# # mylist = ['banana', 'cherry', 'apple']
# # print(mylist)
# #
# # # create an empty list
# # mylist02 = list()
# #
# # # check if the item is in the list
# # if 'banana' in mylist:
# #     print('banana')
# # else:
# #     print('No it is not in the list')
# #
# # mylist.append('kiwi')
# # print(mylist)
# # mylist.insert(1,'orange')
# # print(mylist)
# # mylist.remove('banana')
# # print(mylist)
# # mylist.pop()
# # print(mylist)
# #
# # # remove needs an value to remove or else returns an value error
# # # pop just removes the last element if the index is not mentioned.
# # # mylist.clear() -- empty the list
# #
# # print(type(mylist[0]))
# # mylist02 = [1,2,3,4]
# # print(type(mylist02[0]))
# # mylist03 = [1,2,3,4,'data']
# # print(type(mylist03[-1]))
# #
# # a = [1,2,3]
# # b = [4,5,6]
# # print(a+b)
#
# # Tuples
#
# mytuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
# print(mytuple)
# # it is a better practice to put ,(comma) if there is only a single element.
# mytuple02 = ('a','b','c','a','b','c','a','b','c','a','b','c')
# print(mytuple02.count('a'))
# # convert tuple to list
# mylist = list(mytuple02)
# print(mylist)
#
# # tuples are more efficient when we know that there is no need of changing values
# import sys
# print(sys.getsizeof(mylist), "bytes")
# print(sys.getsizeof(mytuple02), "bytes")
# # tuple takes less space compared to list
#
# import timeit
# print(timeit.timeit(stmt='[0,1,2,3]', number=100))
# print(timeit.timeit(stmt='(0,1,2,3)', number=100))

# # dictionaries
# mydict = {'name':'nikhil', 'age':25}
# print(mydict)
# for key, value in mydict.items():
#     print(key, value)
#
# for key in mydict.keys():
#     print(key)

# set
#
# myset = set([1,2,3,4,5,6,7,8,9])
# print(myset)

# odd = {1,3,5,7,9}
# even = {2,4,6,8}
# primes = {2,3,5,7}
#
# print(odd.union(even))
# print(odd.intersection(even))
# print(odd.difference(even))
# print(odd.union(primes))
# print(odd.intersection(primes))
# even.update(odd)
# print(even)

# Strings

mystring = "Nikhil"
print(mystring[::-1]) # reverse string
#
# for i in mystring:
#     print(i)

ch = ""
for i in mystring:
    ch = i + ch
print(ch)
for i in ch:
    print(i)
mystring.lower()
mystring.upper()
mystring.strip()
mystring.endswith('l')
mystring.find('l')
mystring.index('l')
mystring.count('l')

new_str = 'how are you doing'
mylist = new_str.split(' ')
print(mylist)
mystr = ' '.join(mylist)
print(mystr)

var = 3.45
s = 'the variable is %.2f'% var
print(s)
print(f"{var} is the variable")










