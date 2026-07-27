# Assignment 10: Pandas Fundamentals

## Overview

This assignment focuses on learning the fundamentals of the Pandas library for data analysis in Python. It covers Series, DataFrames, indexing, filtering, sorting, grouping, plotting, and applying these concepts to a simple sales data analysis project.

---

## Topics Covered

- Pandas Introduction
- Series
- DataFrames
- Indexing (`loc` & `iloc`)
- Arithmetic Operations
- Series Methods
- DataFrame Exploration
- Data Filtering
- Sorting Data
- GroupBy Operations
- Pandas Plotting
- Sales Data Analysis

---

## Folder Structure

```text
Gen-AI (Assignment 10) - Nishant Saini/
│
├── Assignment.ipynb
└── README.md
```

---

## Task 1: Series Basics

### Objective

Create and explore a Pandas Series.

### Features

- Create a Series
- Display Series values
- View index
- Check data type
- Access elements using indexing
- Slice a Series

### Concepts Used

- `pd.Series()`
- `index`
- `dtype`
- `loc`
- `iloc`

---

## Task 2: Series Arithmetic Operations

### Objective

Perform arithmetic operations on a Series.

### Features

- Addition
- Subtraction
- Multiplication
- Division

### Concepts Used

- Arithmetic Operators
- `.add()`
- `.sub()`

---

## Task 3: Series Analysis

### Objective

Analyze student marks using Series methods.

### Features

- Maximum marks
- Minimum marks
- Average marks
- Total marks
- Pass/Fail classification
- Count passed students

### Concepts Used

- `max()`
- `min()`
- `mean()`
- `sum()`
- `apply()`
- `lambda`

---

## Task 4: DataFrame Basics

### Objective

Create and explore a DataFrame.

### Features

- Create a DataFrame
- Display records
- Display first three rows
- Display last two rows
- View columns
- View DataFrame shape

### Concepts Used

- `pd.DataFrame()`
- `head()`
- `tail()`
- `columns`
- `shape`

---

## Task 5: DataFrame Exploration

### Objective

Explore and summarize a DataFrame.

### Features

- Dataset information
- Descriptive statistics
- Display first and last records
- Sort values
- Reset index

### Concepts Used

- `info()`
- `describe()`
- `sort_values()`
- `reset_index()`

---

## Task 6: Data Filtering

### Objective

Filter records using different conditions.

### Features

- Students scoring above 75
- Students studying Math
- Students scoring above average
- Students scoring below 70

### Concepts Used

- Boolean Indexing
- Comparison Operators
- `mean()`

---

## Task 7: GroupBy Operations

### Objective

Analyze grouped data.

### Features

- Average marks by subject
- Count students by subject
- Highest marks by subject

### Concepts Used

- `groupby()`
- `mean()`
- `count()`
- `max()`

---

## Task 8: Pandas Plotting

### Objective

Visualize data using Pandas built-in plotting methods.

### Features

- Bar Chart
- Line Chart
- Histogram

### Concepts Used

- `DataFrame.plot()`
- `Series.plot()`

> **Note:** Only Pandas plotting methods were used. No direct Matplotlib customization was required.

---

## Task 9: Mini Sales Data Analysis

### Objective

Analyze a simple sales dataset using Pandas.

### Features

- Calculate total revenue
- Calculate average revenue
- Find the day with the highest revenue
- Filter days with revenue above average
- Visualize revenue using a bar chart

### Concepts Used

- `sum()`
- `mean()`
- `max()`
- Boolean Filtering
- `plot()`

---

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd "Gen-AI (Assignment 10) - Nishant Saini"
```

### 3. Install Required Libraries

```bash
pip install pandas matplotlib notebook
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open **Assignment.ipynb** and run the cells sequentially.

---

## Learning Outcomes

After completing this assignment, I learned:

- How to work with Pandas Series and DataFrames
- How to access and manipulate tabular data efficiently
- How to perform statistical operations on datasets
- How to filter and sort data using different conditions
- How to analyze grouped data using `groupby()`
- How to visualize data using Pandas plotting methods
- How to apply Pandas concepts to solve simple real-world data analysis problems

---

## Technologies Used

- Python 3
- Pandas
- Jupyter Notebook

---

## Author

**Nishant Saini**  
B.Tech Computer Engineering  
Government Engineering College, Ajmer