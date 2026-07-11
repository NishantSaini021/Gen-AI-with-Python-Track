# Task 5. Create Product info file (User input)  
with open("products.txt", "w") as file:
    i = 0
    while i < 3:
        name = input("Enter Product name: ")
        price = input("Enter Price of Product: ")
        file.write(f"{name}|{price}\n")
        i += 1

with open("products.txt", "r") as file:
    for line in file:
        name, price = line.strip().split("|")
        print(f"Product: {name}, Price: {price}")