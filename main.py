import streamlit as st
import time

# --- simple meditation web app -- 
# --- MEDITATEME --- 

def set_stage(i):
    st.session_state.stage = i
# end function

def home_screen():

    st.title("Meditate Me ")
    st.divider()
    
    meditation_time = st.slider("Meditation Time (minutes)", 1, 90 ,5 )
    break_time = st.slider("Break Time", 1, 30, 5)

    if st.button("Start Meditation"):
        timer(meditation_time, break_time)
    
    

def timer(meditation_time, break_time):
    meditation_seconds = meditation_time*60
    break_seconds = break_time*60

    med_placeholder = st.empty()
    break_placeholder = st.empty()

    med_placeholder.write("Meditate")
    for i in range(meditation_seconds):
        time.sleep(1)
        med_placeholder.write(f"{meditation_seconds - i} seconds left")
    # next i

    break_placeholder.write("Rest!")
    for i in range(break_seconds):
        time.sleep(i)
        break_placeholder.write(f"{break_seconds-i} seconds left")
    # next i
# end function

home_screen()


    