import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 7, 5

import matplotlib.pyplot as plt

x = [i for i in range(-100, 105, 5)]
y = [i**2 for i in x]

# Create basic plot
plt.plot(x, y)

# Show plot
plt.show()

