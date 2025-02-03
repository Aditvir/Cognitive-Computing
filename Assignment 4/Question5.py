import numpy as np

# Creating the 2D array
ucs420_Aditvir = np.array([[10, 20, 30, 40],
                           [50, 60, 70, 80],
                           [90, 15, 20, 35]])

# Computing statistics
mean_value = np.mean(ucs420_Aditvir)
median_value = np.median(ucs420_Aditvir)
max_value = np.max(ucs420_Aditvir)
min_value = np.min(ucs420_Aditvir)
unique_elements = np.unique(ucs420_Aditvir)

# Reshaping the array to 4x3
reshaped_ucs420_Aditvir = ucs420_Aditvir.reshape(4, 3)

# Resizing the array to 2x3 (modifying original array)
resized_ucs420_Aditvir = np.resize(ucs420_Aditvir, (2, 3))

# Printing results
print("Mean:", mean_value)
print("Median:", median_value)
print("Max:", max_value)
print("Min:", min_value)
print("Unique Elements:", unique_elements)
print("Reshaped Array (4x3):\n", reshaped_ucs420_Aditvir)
print("Resized Array (2x3):\n", resized_ucs420_Aditvir)
