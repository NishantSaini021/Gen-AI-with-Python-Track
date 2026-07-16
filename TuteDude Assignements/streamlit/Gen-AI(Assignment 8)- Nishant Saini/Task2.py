# Task 2. Price Calculator
import streamlit as st
price = st.number_input("Enter Price: ", min_value = 0)
dicount = st.slider("Select Discount Percentage", 0,50,0)
click = st.button("Calculate Dicounted Price")
pad = price - price*dicount/100
if click:
    st.success(f"Original Price: {price}")
    st.success(f"Discount: {dicount}%")
    st.success(f"Final Price: {pad}")
