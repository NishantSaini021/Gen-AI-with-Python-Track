````markdown
# Assignment 8: Streamlit Basics

## Overview

This assignment focuses on building simple interactive web applications using Streamlit. The tasks cover user input, buttons, sliders, select boxes, sidebars, metrics, tables, and charts.

---

## Topics Covered

- Streamlit Setup
- Titles and Text
- User Input Widgets
- Buttons
- Number Inputs
- Sliders
- Select Boxes
- Sidebar Components
- Success Messages
- Metrics
- Tables
- Bar Charts

---

## Folder Structure

```text
Gen-AI(Assignment 8)- Nishant Saini/
│
├── app_basic.py
├── app_discount.py
├── app_product_form.py
├── app_dashboard.py
└── README.md
```

---

## Task 1: Basic Streamlit App

### Objective

Create a simple greeting application.

### Features

- Displays a title
- Accepts user name input
- Uses a button to trigger an action
- Greets the user dynamically

### Components Used

- `st.title()`
- `st.text_input()`
- `st.button()`
- `st.write()`

---

## Task 2: Price Calculator

### Objective

Calculate the discounted price of a product.

### Features

- Accepts product price
- Allows discount selection using a slider
- Calculates final price
- Displays results using success messages

### Components Used

- `st.number_input()`
- `st.slider()`
- `st.button()`
- `st.success()`

### Formula Used

```python
final_price = price - (price * discount / 100)
```

---

## Task 3: Product Form

### Objective

Create a product entry form using the Streamlit sidebar.

### Features

- Product name input
- Category selection
- Product price input
- Product addition confirmation
- Product details display

### Components Used

- `st.sidebar.text_input()`
- `st.sidebar.selectbox()`
- `st.sidebar.number_input()`
- `st.sidebar.button()`
- `st.success()`
- `st.write()`

---

## Task 4: Mini Sales Dashboard

### Objective

Display monthly sales information using a dashboard.

### Features

- Month selection
- Display selected month's sales
- Visualize sales data using a bar chart

### Components Used

- `st.title()`
- `st.selectbox()`
- `st.metric()`
- `st.bar_chart()`

### Sales Data

```python
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}
```

---

## How to Run

### 1. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 2. Run Any Task

Task 1:

```bash
streamlit run app_basic.py
```

Task 2:

```bash
streamlit run app_discount.py
```

Task 3:

```bash
streamlit run app_product_form.py
```

Task 4:

```bash
streamlit run app_dashboard.py
```

### 3. Open in Browser

Streamlit will provide a local URL:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## Learning Outcomes

After completing this assignment, I learned:

- How to build web applications using Streamlit
- How to collect user input interactively
- How buttons trigger actions in Streamlit
- How to use sliders and select boxes
- How to create sidebar forms
- How to display messages and metrics
- How to create simple dashboards
- How to visualize data using charts

---

## Author

**Nishant Saini**  
B.Tech Computer Engineering  
Government Engineering College, Ajmer
````
