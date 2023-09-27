import streamlit as st
import time

# --- simple meditation web app -- 
# --- MEDITATEME --- 

def set_stage(i):
    st.session_state.stage = i
# end function

def make_sidebar():
    with st.sidebar:
        st.title("Navigation")
        st.markdown("#####")
        st.button("Home", on_click=set_stage, args=[0], use_container_width=True)
        st.button("How to Meditate", on_click=set_stage, args=["1"], use_container_width=True)  
        st.button("Other Resourses", on_click=set_stage, args=["2"], use_container_width=True) 
        st.button("Help", on_click=set_stage, args=[3],use_container_width=True)
# end function

def home_screen():

    if "stage" not in st.session_state:
        st.session_state.stage = 0

    if st.session_state.stage == 0:
        st.title("Meditate Me ")
        st.divider()
        make_sidebar()
        
        meditation_time = st.slider("Meditation Time (minutes)", 0, 90 ,5 )
        break_time = st.slider("Break Time", 1, 30, 5)

        if st.button("Start Meditation"):
            timer(meditation_time, break_time)
    # end if
# end function
    

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


    