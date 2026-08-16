import streamlit as st

st.set_page_config(
    page_title="My App",
    layout="wide"
)

page = st.sidebar.radio(
    "Pages",
    [
        "Home",
        "Dashboard",
        "Projects",
        "Profile"
    ]
)

if page == "Home":
    st.title("Home")

elif page == "Dashboard":
    st.title("Dashboard")

elif page == "Projects":
    st.title("Projects")

elif page == "Profile":
    st.title("Profile")