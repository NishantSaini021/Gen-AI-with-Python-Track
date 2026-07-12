#Task1. Safe division utility
try:
    x = float(input("Enter numerator: "))
    y = float(input("Enter denominator: "))
    result =(x/y)
except ValueError:
    print("Invalid input, please enter valid number")
except ZeroDivisionError:
    print("Division from zero is not possible")
else:
    print(f"Result: {result}")
finally:
    print("Operation completed")