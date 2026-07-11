# Assignment 4 - File Handling in Python

## Overview

This assignment focuses on understanding and implementing Python File Handling concepts. The tasks cover creating, reading, updating, and processing data stored in text files using built-in Python functions.

---

## Tasks Completed

### Task 1: Write Sales Records to a File
- Created a list of sales amounts.
- Opened a text file in write mode.
- Wrote each sales amount on a separate line.
- Reopened the file and displayed its contents.

### Task 2: Read File in Different Ways
- Read the complete file using `read()`.
- Read the first line using `readline()`.
- Read all lines using `readlines()`.
- Removed newline characters using `strip()`.
- Converted string values into integers.

### Task 3: Append New Sales
- Opened the existing file in append mode.
- Added new sales records.
- Reopened and displayed the updated file contents.

### Task 4: Generate Summary Report
- Read all sales values from the file.
- Converted file data into integers.
- Calculated:
  - Total Sales
  - Highest Sale
  - Lowest Sale
  - Average Sale

### Task 5: Create Product Information File
- Accepted product names and prices from the user.
- Stored product information in a text file.
- Read and displayed the stored product data.

### Task 6: Read File Safely
- Accepted a filename from the user.
- Checked file existence using `os.path.exists()`.
- Opened and displayed file contents if the file existed.
- Displayed an error message when the file was not found.

### Task 7: Mini Project - Export Discounted Prices
- Stored product prices using a dictionary.
- Accepted a discount percentage from the user.
- Calculated discounted prices.
- Exported the report to a text file.
- Read and displayed the generated report.
- Calculated:
  - Total Products
  - Average Discounted Price

---

## Concepts Used

- File Handling
- Reading Files
- Writing Files
- Appending Files
- Context Managers (`with open`)
- String Manipulation
- Lists
- Dictionaries
- Loops
- Conditional Statements
- User Input
- Data Conversion (`int()`)
- `os.path.exists()`
- Basic Data Processing

---

## Learning Outcomes

Through this assignment, I learned:

- How to create and manage text files in Python.
- Different ways to read file data.
- How to append new information to existing files.
- Converting file data from strings to integers.
- Generating reports from stored data.
- Checking file existence before opening files.
- Combining file handling with loops, lists, and dictionaries to build small practical projects.

---

## Technologies Used

- Python 3

---

## Folder Structure

```
Assignment-4-FileHandling/
│
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.py
├── Task5.py
├── Task6.py
├── Task7.py
├── sales_data.txt
├── products.txt
├── discount_report.txt
└── README.md
```


## How to Run

### Prerequisites

- Python 3 installed on your system

### Running the Programs

1. Open a terminal in the project folder.

2. Run any task file using:

```bash
python Task1.py
```

or

```bash
python Task2.py
```

or any other task file:

```bash
python Task3.py
python Task4.py
python Task5.py
python Task6.py
python Task7.py
```

### Notes

- Task 1 creates `sales_data.txt`.
- Task 3 appends additional sales records to `sales_data.txt`.
- Task 5 creates `products.txt`.
- Task 7 generates `discount_report.txt`.
- Some tasks require user input through the terminal.
---

## Author

Nishant Saini  
Computer Engineering Student