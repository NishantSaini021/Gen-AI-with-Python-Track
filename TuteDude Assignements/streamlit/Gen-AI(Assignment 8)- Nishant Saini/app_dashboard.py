# Task 4. Mini Dashboard
import streamlit as st
st.title("Simple Sales Dashboard")
st.write("The Dashboard is fo Sales Details")
month = st.selectbox("Month", ["January", "February", "March", "April"])
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}
show = st.button("Show Sales")
if show:
    # st.write(f"Sales: {sales[month]}")
    st.metric(label = "Sales", value = sales[month])
st.bar_chart(list(sales.values()))
