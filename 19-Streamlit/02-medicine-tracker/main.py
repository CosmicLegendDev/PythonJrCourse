import streamlit as st

# 1. Define pages
home_page = st.Page("pages/home.py", title="Home", icon="🏠")
list_page = st.Page("pages/medicines.py", title="Medicines", icon="💊")
add_med = st.Page("pages/add.py", title="Add", icon="➕")
profile_page = st.Page("pages/profile.py", title="Profile", icon="⚙️")

# 2. Setup navigation with built-in menu (sidebar or top)
pg = st.navigation(
    {
        "Main": [home_page, list_page, add_med],
        "Account": [profile_page],
    },
    position="sidebar",  # Options: "sidebar" or "top"
)

# 3. Run the selected page
pg.run()