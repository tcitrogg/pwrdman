# import our modules
import streamlit as st

vault = {}

# gui
create_tab, fetch_tab = st.tabs(["Create", "Fetch"])

with create_tab:
    account_name = st.text_input("Account Name", key="create_tab").lower()
    usrname = st.text_input("Username")
    generate_btn = st.button("Generate")
    if generate_btn:
       passwrd = gen_passwrd()
       st.code(passwrd)
       

with fetch_tab:
    account_name = st.text_input("Account Name", key="fetch_tab").lower()
    fetch_btn = st.button("Fetch")