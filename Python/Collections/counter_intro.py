# collections
# Counter -- acts like dictionary and keywords as well like, items, keys, values,
# namedtuple
# OrderedDict
# defaultdict
# deque

from collections import Counter

a = 'aaaaaabbbbccccc'
my_counter = Counter(a)
print(my_counter)

# b = my_counter.most_common()
# print(b)

s = 'aaaabbbbcccc'
my_counter02 = Counter(s)
print(my_counter02.keys())
print(my_counter02.values())
print(my_counter02.items())
print(my_counter02.most_common(2))

print(my_counter02.elements()) # this gives us an iterable so we convert this into a list.
print(list(my_counter02.elements()))