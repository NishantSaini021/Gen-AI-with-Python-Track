# Task2. Read File in Different ways
with open("sales_data.txt", "r") as file:
    data = file.read()
    file.seek(0)
    line_data = file.readline()
    file.seek(0)
    lines = file.readlines()
    lines_data = []
    for val in lines:
        lines_data.append(int(val.strip()))

print("Using read():")
print(data)

print("Using readline():")
print(line_data)

print("Using readlines():")
print(lines_data)