# import our modules
import streamlit as st
# import pwrd
from pwrd import Pwrd

pd = Pwrd()

# gui
create_tab, fetch_tab = st.tabs(["Create", "Fetch"])

with create_tab:
    account_name = st.text_input("Account Name", key="create_tab").lower()
    usrname = st.text_input("Username")
    generate_btn = st.button("Generate")
    if generate_btn:
       passwrd = pd.gen_passwrd()
       pd.store(account_name, usrname, passwrd)
       st.code(passwrd)
       

with fetch_tab:
    account_name = st.text_input("Account Name", key="fetch_tab").lower()
    fetch_btn = st.button("Fetch")
    if fetch_btn and len(account_name) != 0:
        result = pd.fetch_account(account_name)
        if result == False:
            st.error("Invalid Account")
        else:
            st.code(result)