import streamlit as st
from db.meddb import med_db

st.title("Its a add medicine page.")

# 1. Create a form container using the 'with' statement
with st.form(key="medicine_form"):
    st.subheader("Please enter medicine details")
    
    # 2. Add single-line text inputs
    med_name = st.text_input(label="Medicine Name", placeholder="e.g. Paracetamel")
    med_quantity = st.text_input(label="Quantity", placeholder="e.g. 3")
    med_expiry = st.text_input(label="Expiered On", placeholder="e.g. 26 Jun, 2027")
    
    # 4. Add the mandatory submit button
    submit_button = st.form_submit_button(label="Submit")

# 5. Process the form data after submission
if submit_button:
    if med_name and med_quantity and med_expiry:
        med_db.add(med_name=med_name, med_quantity=med_quantity, med_expire=med_expiry)
        st.success("Medicine Added successfully to inventory!")
    else:
        st.error("Please fill out all fields.")