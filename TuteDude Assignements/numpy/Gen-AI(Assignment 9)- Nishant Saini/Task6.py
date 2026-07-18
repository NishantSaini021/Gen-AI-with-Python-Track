# Task 6. Precntiles and Sorting
import numpy as np
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
print(np.sort(marks))
print(np.percentile(marks, 25))
print(np.percentile(marks, 50))
print(np.percentile(marks, 75))
avg = np.mean(marks)
print(len(marks[marks>avg]))