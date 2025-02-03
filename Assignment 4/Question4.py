import numpy as np

# Create a 1-D array with 25 values from 10 to 100
my_array = np.linspace(10, 100, 25)

# Print array details
print("Array:", my_array)
print("Dimensions:", my_array.ndim)
print("Shape:", my_array.shape)
print("Total Elements:", my_array.size)
print("Data Type:", my_array.dtype)
print("Memory (Bytes):", my_array.nbytes)

# Reshape the array into a column (25 rows, 1 column)
reshaped_array = my_array.reshape(25, 1)
print("\nReshaped Array:\n", reshaped_array)

# Check the effect of .T (Transpose)
print("\nUsing .T:", my_array.T)
print("Shape after .T:", my_array.T.shape)

# Explanation
print("\n.T does not change a 1-D array since it has only one dimension.")