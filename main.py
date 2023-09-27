import streamlit as st

# --- simple meditation web app -- 
# --- MEDITATEME --- 

def home_screen():
    st.title("MediatateMe")
    st.divider()

    # active use number at the top
    # running count of how many have used it to date

    # make the main feature - circular time that contains 3 default settings and a custom setting 3 mins, 5 mins, 20 mins , custom