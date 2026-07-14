import streamlit as st

st.title("Hello Nishant")
st.subheader("Sub Heading")
st.write("My first Streamlit app")
st.text("Streamlit Text")

y = st.selectbox("Select Number:", ["_","1", "2", "3", "4", "5", "6"])
st.write(f"You selected {y} Excellent choice")
st.checkbox("Confirm")
if st.button("Confirm"):
    st.success("Your number was succesfuly selected")