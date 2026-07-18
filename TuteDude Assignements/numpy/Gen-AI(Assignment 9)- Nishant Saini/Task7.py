# Task 7. Mini Use Case: Sales Analysis
import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])
print(f"Total Weekly Sales: {np.sum(sales)}")
print(f" Average Daily Sales: {np.mean(sales)}")
highest_day = np.where(sales == np.max(sales))[0][0] + 1
print(f"Highest Sales Day: Day {highest_day}")
lowest_day = np.where(sales == np.min(sales))[0][0] + 1
print(f"Lowest Sales Day: Day {lowest_day}")
print(f" Standard Deviation of Sales: {np.std(sales)}")
above_avg_days = np.where(sales > np.mean(sales))[0] + 1
print(f"Above Average Days: {above_avg_days}")