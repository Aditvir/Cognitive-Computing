import numpy as np

arr = np.array([[10, 20, 30], 
                [40, 50, 60], 
                [70, 80, 90]])

value_1 = arr[0][1]
value_2 = arr[2][0]

print("a) 1st row, 2nd column:", value_1)
print("b) 3rd row, 1st column:", value_2)