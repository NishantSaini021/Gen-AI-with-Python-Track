# Assignment 5: Modules, Packages & Imports

## Overview

This assignment demonstrates the use of Python modules, packages, and different import methods. The project is organized into reusable modules and a package to improve code structure and maintainability.

---

## Folder Structure

```text
Modules_assignment/
│
├── main.py
├── math_utils.py
├── string_utils.py
├── README.md
│
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py
```

---

## Tasks Completed

### Task 1: math_utils Module

Created a module containing:

- add(a, b)
- subtract(a, b)
- square(n)

Tested using:

```python
import math_utils
from math_utils import square
```

---

### Task 2: string_utils Module

Created a module containing:

- capitalize_words(text)
- reverse_string(text)
- word_count(text)

Tested all functions in `main.py`.

---

### Task 3: shop_package Package

Created a package named `shop_package` containing:

#### discount.py

- apply_discount(price, percent)
- flat_discount(price)

#### billing.py

- calculate_total(prices)
- apply_tax(amount)

#### __init__.py

Used to define the package and export package functions.

---

### Task 4: Importing Package Functions

Imported package functions using:

```python
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax
```

Tested all package functions successfully.

---

## Concepts Practiced

- Creating Python modules
- Importing modules
- Importing specific functions
- Using aliases during import
- Creating packages
- Using __init__.py
- Organizing code into reusable components
- Working with functions across multiple files

---

## How to Run

1. Open a terminal in the project folder.

2. Run:

```bash
python main.py
```

3. The program will execute and display outputs from:
   - math_utils.py
   - string_utils.py
   - shop_package

---

## Output Demonstrates

- Mathematical operations
- String manipulation
- Discount calculations
- Billing calculations
- Package imports and usage

---

## Author

**Nishant Saini**  
Computer Engineering Student  
Government Engineering College, Ajmer