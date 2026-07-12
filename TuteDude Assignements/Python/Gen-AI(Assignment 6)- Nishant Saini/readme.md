# Assignment 6: Exception Handling

## Overview

This assignment focuses on Python Exception Handling concepts. The tasks demonstrate how to handle runtime errors, validate user input, create custom exceptions, and ensure programs continue running safely when unexpected situations occur.

---

## Topics Covered

- try and except
- Multiple exception blocks
- else block
- finally block
- Raising exceptions using raise
- Custom exceptions
- ValueError
- ZeroDivisionError
- TypeError
- FileNotFoundError
- PermissionError

---

## Folder Structure

```text
Gen-AI(Assignment 6)- Nishant Saini/
│
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.py
├── Task5.py
├── test.txt
└── README.md
```

---

## Task 1: Safe Division Utility

### Objective
Create a program that safely performs division while handling invalid inputs.

### Concepts Practiced
- ValueError
- ZeroDivisionError
- else block
- finally block

### Features
- Takes numerator and denominator as input
- Handles non-numeric inputs
- Prevents division by zero
- Displays result when no exception occurs
- Prints "Operation Complete" using finally

---

## Task 2: Bill Calculator with Error Handling

### Objective
Process a list of product prices while handling invalid entries.

### Concepts Practiced
- TypeError
- ValueError
- raise statement

### Features
- Iterates through product prices
- Skips invalid entries
- Raises error for negative prices
- Calculates total of valid prices
- Continues execution after errors

---

## Task 3: Custom Exception – Age Validator

### Objective
Validate age using a custom exception.

### Concepts Practiced
- Creating custom exceptions
- raise
- Custom exception handling

### Features
- Accepts user age
- Ensures age is between 1 and 120
- Raises custom exception when invalid
- Displays meaningful error messages

---

## Task 4: File Reader with Exception Handling

### Objective
Safely read data from a file.

### Concepts Practiced
- FileNotFoundError
- PermissionError
- finally block

### Features
- Accepts filename from user
- Reads and prints first three lines
- Handles missing files
- Handles permission issues
- Ensures operation status is displayed

---

## Task 5: Safe Shopping Cart

### Objective
Create a shopping cart that safely accepts product prices.

### Concepts Practiced
- Custom exceptions
- Input validation
- Lists
- Loops
- Exception handling

### Features
- Accepts prices until user enters 'q'
- Handles invalid input
- Prevents negative prices
- Stores valid prices in cart
- Displays total items and total bill

---

## How to Run

Open a terminal inside the assignment folder and run:

```bash
python Task1.py
```

or

```bash
python Task2.py
```

or

```bash
python Task3.py
```

or

```bash
python Task4.py
```

or

```bash
python Task5.py
```

---

## Learning Outcomes

After completing this assignment, I learned:

- How to use try and except blocks
- How to handle multiple exceptions
- How else and finally work
- How to raise exceptions manually
- How to create custom exceptions
- How to write safer and more reliable Python programs
- How to validate user input effectively

---

## Author

**Nishant Saini**  
Computer Engineering Student  
Government Engineering College, Ajmer