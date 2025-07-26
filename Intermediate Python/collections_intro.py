# Counter
# namedtuple
# Ordereddict
# defaultdict
# deque

# Counter - conatainer stores elements as dict keys stores ele - values

# from collections import Counter
#
# s = 'aaabbbbccccc'
# count = Counter(s)
# new_str = ''
# for letter, count in count.items():
#     new_str += letter + str(count)
#
# print(new_str)

# namedtuple - creating a simple named objects
# from collections import namedtuple
#
# point = namedtuple("Point", 'x,y')
# pt = point(10,20)
# print(pt.x, pt.y)

#OrderedDict remembers the order but not that important used in older versions
# from collections import OrderedDict
#
# ord_dct = OrderedDict()
# ord_dct['a'] = 1
# ord_dct['b'] = 2
# ord_dct['c'] = 3
# ord_dct['d'] = 4
# print(ord_dct)

# defaultdict - only kind of values can be entered int - int period.
# from collections import defaultdict
#
# # you can assign default values to the default dict
#
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['a'])

# deque can be used add elements from both sides

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([4,5,7])
print(d)
d.rotate(2)
print(d)