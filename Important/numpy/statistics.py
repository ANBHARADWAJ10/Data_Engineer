import numpy as np

stats = np.array([[1,2,3],[4,5,6]])

print(np.max(stats[0]))
print(np.min(stats[1]))
print(np.max(stats))
print(np.min(stats, axis = 0))
print(np.sum(stats, axis = 0))


