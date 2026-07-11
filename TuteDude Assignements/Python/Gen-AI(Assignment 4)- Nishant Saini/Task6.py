# Task 6. Read the file safely(error handling inside file handling only)
name = input("Which file you want to open: ")
import os

if os.path.exists(name):
    with open (name, "r") as file:
        print(file.read())
else:
    print("File not found")
print(type(os.path.exists(name)))