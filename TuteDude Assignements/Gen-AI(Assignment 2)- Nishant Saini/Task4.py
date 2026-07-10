# Task 4 named Task 5 in given document
daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break

    if sale == 0:
        print("No sales today. Skipping.")
        continue

    total_sales += sale

    print("Added:", sale)
    print("Running Total:", total_sales)

print("Final Total Sales:", total_sales)