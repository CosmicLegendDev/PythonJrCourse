import streamlit as st

st.title(" Home Medicine Tracker system ")
st.image("assets/medicine_pic.png")

profile_name = st.session_state.get("profile_name", "")
if profile_name == "":
    st.warning("Please enter your name in the profile page to continue.")
else:
    st.success(f"Welcome {profile_name} to the medicine tracker system.")