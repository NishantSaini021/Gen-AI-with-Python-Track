# Task 4. Aggergation Operations
import numpy as np
matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(np.sum(matrix, axis = 1))
print(np.sum(matrix, axis=0))
print(np.min(matrix))
print(np.max(matrix))
print(np.mean(matrix))