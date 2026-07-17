# Task 2. Price Calculator
import streamlit as st
price = st.number_input("Enter Price: ", min_value = 0)
discount = st.slider("Select Discount Percentage", 0,50,0)
click = st.button("Calculate Discounted Price")
pad = price - price*discount/100
if click:
    st.success(f"Original Price: {price}")
    st.success(f"Discount: {discount}%")
    st.success(f"Final Price: {pad}")
if click:
    st.table([
        ["Original Price", price],
        ["Discount", f"{discount}%"],
        ["Final Price", pad]
    ])