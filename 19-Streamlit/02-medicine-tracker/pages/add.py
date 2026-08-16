import streamlit as st

st.title("Its a add medicine page.")

input_name = st.text_input("Enter medicine name")
input_amount = st.number_input("Enter amount", min_value=1, step=1)

