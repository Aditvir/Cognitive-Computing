# a) reverse the numpy array
import numpy as np

arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]

print(reversed_arr)

# b) (i) x = np.array([1,2,3,4,5,1,2,1,1,1])
x = np.array([1,2,3,4,5,1,2,1,1,1])
values, counts = np.unique(x, return_counts=True)
most_frequent_value = values[np.argmax(counts)]
indices = np.where(x == most_frequent_value)[0]

print("Most Frequent Value:", most_frequent_value)
print("Indices:", indices) 

# b) (ii) y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
values, counts = np.unique(y, return_counts=True)
most_frequent_value = values[np.argmax(counts)]
indices = np.where(y == most_frequent_value)[0]

print("Most Frequent Value:", most_frequent_value)
print("Indices:", indices)