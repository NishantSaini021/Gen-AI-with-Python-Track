#Task 3. Product Form
import streamlit as st

name = st.sidebar.text_input("Enter Product Name")

category = st.sidebar.selectbox(
    "Select Category",
    ["Electronics", "Hardware", "Automobile", "Art and Craft", "Sports"]
)

price = st.sidebar.number_input(
    "Enter Price",
    min_value=0
)

if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully!")

    st.write("## Product Details")
    st.write(f"Product Name: {name}")
    st.write(f"Category: {category}")
    st.write(f"Price: ₹{price}")

