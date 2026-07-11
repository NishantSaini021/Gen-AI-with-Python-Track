# Task 3. Append new sales
with open ("sales_data.txt", "a") as file:
    new_sales = [5000, 2500, 1700]

    for sale in new_sales:
        file.write(f"\n{sale}")
with open ("sales_data.txt", "r") as file:
    data = file.read()
print(data)
