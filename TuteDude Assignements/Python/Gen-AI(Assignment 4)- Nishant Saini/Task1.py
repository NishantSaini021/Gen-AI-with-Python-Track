# Task1. Write sales record to file

sales = [1200,450,980,1500,3000]
file = open("sales_data.txt", "w")
for val in sales:
    file.write(f"{val}\n")
file.close()
