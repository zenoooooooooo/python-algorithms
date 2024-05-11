from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

import math
ages = [6, 5, 4, 6, 5, 5, 4, 7, 5]
mean = np.mean(ages)

variance = 0
differences = []

for num in ages:
    differences.append(num - mean)

squared_differences = []

for num in differences:
    squared_differences.append(num ** 2)

variance = np.mean(squared_differences)

standard_variation = math.sqrt(variance)

print('Datas:', ages)
print('Mean', mean)
print('Variance:', variance)
print('Standard Variation:', standard_variation)
print('Variance:', np.var(ages))

# incomes = np.random.normal(100.0, 50.0, 10000)

# plt.hist(incomes, 20)
# plt.show()

# So these methods are only usable on NumPy lists/arrays!

x = np.arange(-5, 5, 0.1)
plt.plot(x, norm.pdf(x))
plt.show()