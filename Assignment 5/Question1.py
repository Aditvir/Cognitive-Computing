import numpy as np
import matplotlib.pyplot as plt 

matrix = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
total_sum = np.sum(matrix)
row_wise_sum = np.sum(matrix, axis=1)
col_wise_sum = np.sum(matrix, axis=0)

print("Sum of all elements: ", total_sum)
print("Sum of all elements row-wise: \n", row_wise_sum)
print("Sum of all elements column-wise: \n", col_wise_sum)
