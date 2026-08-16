import streamlit as st
from db.meddb import med_db
st.title("List of the medicines in stock")

st.table(med_db.fetch())