import streamlit as st

st.title("List of the medicines in stock")
data = {
    "Medicine": ["Paracetamol", "Pantab", "Vicks"],
    "Quantity": [4, 6, 1],
    "Expirty": ["30-01-2027", "30-01-2027", "30-01-2027"]
}
st.table(data)