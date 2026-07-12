# Task 4. File Reader with exception handling

name = input("Enter name of file you want to open: ")
try:
    with open(name,"r") as file:
        i = 0
        while i < 3:
            line = file.readline()
            if line == "":
                break
            print(line, end="")
            i += 1
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Can't Access this file without permission")
finally:
    print("File Operation Attempted")