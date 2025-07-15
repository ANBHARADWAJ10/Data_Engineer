from collections import namedtuple

point = namedtuple('Point', ['x', 'y'])
pt = point(1, 2)
print(pt)
print(pt.x, pt.y)