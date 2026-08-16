import streamlit as st
st.title("Your profile settings.")

profile_name = st.text_input("Enter your name")
st.session_state.profile_name = profile_name

print(f"Profile name: {profile_name}")