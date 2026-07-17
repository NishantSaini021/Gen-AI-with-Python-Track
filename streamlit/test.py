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

n_type = st.radio("Select Type of Number: ",["Natural", "Complex", "Integer"])
if n_type:
    st.success(f"You Selected: {n_type}")
s = st.selectbox("Choose Required: ", ["A", "B", "C", "D", "E"])
st.slider("Slider:", 1, 200)
age = st.slider("Select Age", 0, 100)
st.write(age)

ia = st.number_input("Your Age: ", min_value=18, max_value=120)
name = st.text_input("Enter Your Name: ")
if name:
    st.write(f"Thanks {name}")

from datetime import date
dob = st.date_input("Select your Date of birth: ", min_value = date(1900,1, 1))
today = date.today()
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1
st.write(f"Your age is {age}")

col1,col2 = st.columns(2)
with col1:
    st.header("Name")
    v1 = st.write("s1")
    v2 = st.write("s2")
with col2:
    st.header("City")
    c1 = st.write("c1")
    c2 = st.write("c2")

st.image("https://docs.streamlit.io/logo.svg", width = 500)

st.sidebar.text_input("Enter Something: ")
st.sidebar.button("Enter")
with st.expander("Show Names"):
    st.write("""
             1. One
             2. Two
             3. Three
             4.Four
             """)
    