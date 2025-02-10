import numpy as np
import matplotlib.pyplot as plt 

# (a) For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find

import numpy as np

numbers = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_numbers = np.sort(numbers)
sorted_indices = np.argsort(numbers)
smallest_values = np.partition(numbers, 4)[:4]
largest_values = np.partition(numbers, -5)[-5:]

print("i. Sorted array:", sorted_numbers)
print("ii. Indices of sorted array:", sorted_indices)
print("iii. 4 smallest elements:", smallest_values)
print("iv. 5 largest elements:", largest_values)

# (b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find

values = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integer_values = values[values.astype(int) == values]
float_values = values[values.astype(int) != values]

print("i. Integer elements only:", integer_values)
print("ii. Float elements only:", float_values)
