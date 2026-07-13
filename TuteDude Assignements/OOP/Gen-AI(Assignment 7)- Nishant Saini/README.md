# Assignment 7: Object-Oriented Programming (OOP)

## Overview

This assignment focuses on Object-Oriented Programming concepts in Python. The tasks demonstrate how to create classes and objects, implement encapsulation, inheritance, polymorphism, abstraction, operator overloading, and build a mini project using OOP principles.

---

## Topics Covered

- Classes and Objects
- Constructors (`__init__`)
- Attributes and Methods
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Abstract Base Classes (ABC)
- Magic Methods
- Operator Overloading
- Composition

---

## Folder Structure

```text
Gen-AI(Assignment 7)- Nishant Saini/
│
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.py
├── Task5.py
├── Task6.py
├── Task7.py
└── README.md
```

---

## Task 1: Product Class

### Objective
Create a Product class and display product information.

### Concepts Practiced

- Classes
- Objects
- Constructors
- Instance Attributes
- Methods

### Features

- Stores product name, price, and category
- Displays product details using `get_info()`
- Creates multiple product objects

---

## Task 2: Encapsulation

### Objective
Protect product price using getter and setter methods.

### Concepts Practiced

- Encapsulation
- Protected Attributes
- Getter Methods
- Setter Methods

### Features

- Prevents invalid prices
- Retrieves price safely
- Updates price through controlled access

---

## Task 3: Inheritance

### Objective
Create a subclass that extends Product.

### Concepts Practiced

- Inheritance
- Parent Class
- Child Class

### Features

- Reuses Product attributes
- Adds additional attributes
- Demonstrates code reusability

---

## Task 4: Polymorphism

### Objective
Implement different product types with customized behavior.

### Concepts Practiced

- Method Overriding
- Runtime Polymorphism

### Features

- Laptop and Mobile classes override methods
- Common interface with different outputs
- Polymorphic method calls

---

## Task 5: Abstraction

### Objective
Create an abstract payment system.

### Concepts Practiced

- Abstract Base Classes (ABC)
- Abstract Methods
- Abstraction

### Features

- Defines a common payment interface
- Implements Credit Card Payment
- Implements UPI Payment

---

## Task 6: Operator Overloading

### Objective
Overload operators using magic methods.

### Concepts Practiced

- Magic Methods
- Operator Overloading
- `__add__`

### Features

- Adds prices of two Product objects
- Demonstrates custom operator behavior

---

## Task 7: Mini Project – Simple Inventory System

### Objective
Build a small inventory management system using OOP concepts.

### Concepts Practiced

- Composition
- Classes and Objects
- Lists of Objects
- Inventory Management
- Operator Overloading

### Classes Created

#### Product

Stores:

- Name
- Price
- Category

Methods:

- `get_info()`
- `__add__()`

---

#### Inventory

Manages a collection of Product objects.

Methods:

- `add_product()`
- `remove_product()`
- `get_total_value()`
- `show_all_products()`

---

#### Store

Represents a store containing an Inventory object.

Methods:

- `add_new_product()`
- `show_summary()`

---

### Features

- Add products dynamically
- Store products inside inventory
- Display all products
- Calculate total inventory value
- Display store summary
- Validate price input

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

or

```bash
python Task6.py
```

or

```bash
python Task7.py
```

---

## Learning Outcomes

After completing this assignment, I learned:

- How to create and use classes and objects
- How constructors initialize object data
- How encapsulation protects attributes
- How inheritance promotes code reuse
- How polymorphism enables flexible behavior
- How abstraction hides implementation details
- How magic methods work in Python
- How operator overloading customizes operators
- How composition helps build larger systems
- How OOP concepts work together in real projects

---

## Author

**Nishant Saini**  
B.Tech Computer Engineering  
Government Engineering College, Ajmer