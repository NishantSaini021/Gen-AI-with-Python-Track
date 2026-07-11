# Task 4. Generate Summary report from file 
with open("sales_data.txt", "r") as file:
    lines = [line.strip() for line in file]
    summary_list = [int(line) for line in lines]
print(f"Total Sales: {sum(summary_list)}")
print(f"Highest Sale: {max(summary_list)}")
print(f"Lowest Sale: {min(summary_list)}")
print(f"Average Sale: {(sum(summary_list))/len(summary_list)}")