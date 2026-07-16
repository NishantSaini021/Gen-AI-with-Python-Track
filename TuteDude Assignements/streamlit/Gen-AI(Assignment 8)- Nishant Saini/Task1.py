import streamlit as st
st.title("Welcome to Streamlit")
name = st.text_input("Enter Your Name: ")
greet = st.button("Greet Me")
if greet:
    st.write(f"Hello, {name}!")