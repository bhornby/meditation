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
        st.button("How to Meditate", on_click=set_stage, args=[1], use_container_width=True)  
        st.button("Other Resources", on_click=set_stage, args=[2], use_container_width=True) 
        st.button("Help", on_click=set_stage, args=[3],use_container_width=True)
# end function

def home_screen():

    if "stage" not in st.session_state:
        st.session_state.stage = 0

    if st.session_state.stage == 0:
        st.title("Meditate Me")
        st.write("Progressive Meditation for Improved Focus")
        st.divider()
        make_sidebar()
        
        meditation_time = st.slider("Meditation Time (minutes)", 0, 90 ,5 )
        break_time = st.slider("Break Time (minutes)", 0, 30, 5)

        if st.button("Start Meditation"):
            timer(meditation_time, break_time)
    # end if
    
    if st.session_state.stage == 1:
        make_sidebar()
        st.title("Progressive Meditation for Improved Focus")
        st.divider()
        st.subheader("**Introduction**")
        st.markdown("######")
        st.write("Meditation is a powerful practice that can enhance your mental clarity, reduce stress, and improve focus. Similar to progressive overload in the gym, where you gradually increase the resistance to build muscle strength, you can apply a progressive approach to meditation to enhance your concentration and mindfulness. This guide will outline how to meditate and incorporate progressive overload principles into short meditation sessions to boost your focus over time.")
        st.markdown("####")
        st.subheader("Step 1: Setting Up for Meditation")
        st.markdown("######")
        st.write(" - **Choose a Quiet Space**: Find a quiet and comfortable place where you won't be disturbed. Ensure that the lighting and temperature are suitable for your comfort.")
        st.write(" - **Posture**: Sit in a comfortable yet alert posture. You can use a cushion or chair to support your lower back if necessary. Keep your spine straight but not rigid.")
        st.write("- **Time**: Time: Start with short sessions of 3-5 minutes. As you progress, gradually increase the duration to challenge your focus.")
        st.markdown("#")
        st.subheader("Step 2: Basic Technique")
        st.write(" - **Focus on Your Breath**: Close your eyes and start by taking a few deep breaths. Then, let your breath return to its natural rhythm. Pay attention to the sensation of your breath as it enters and leaves your nostrils or the rise and fall of your abdomen.")
        st.write(" - **Acknowledge Thoughts**: Thoughts will naturally arise. Instead of suppressing them, acknowledge them without judgment and gently return your focus to your breath.")
        st.write(" - **Use a Mantra (Optional)**: Some people find it helpful to use a word or phrase as a point of focus, like 'peace' or 'calm.' Repeat your chosen word or phrase in your mind with each breath.")
        st.markdown("#")
        st.subheader("Step 3: Progressive Overload in Meditation")
        st.markdown("######")
        st.write(" - **Increase Session Duration**: Begin with short 5-minute sessions. After a week or two of consistent practice, increase the duration to 10 minutes. Gradually extend your sessions to 15, 20, or even 30 minutes as you become more comfortable.")
        st.write(" - **Introduce Challenges**: As you extend your meditation time, introduce challenges to maintain focus. These could include focusing on your breath for longer periods without distraction or using a more detailed meditation object.")
        st.write(" - **Monitor Progress**:  Keep a meditation journal to track your progress. Note the duration of each session and any challenges you faced. This will help you identify areas where you can apply progressive overload.")
        st.write(" - **Consistency Is Key**: Just like in the gym, consistent practice is essential. Aim to meditate daily or at least several times a week to see meaningful improvements in your focus.")
        st.markdown("#")
        st.subheader("Step 4: Rest and Recovery")
        st.markdown("######")
        st.write(" - **Rest Days**: Just as you need rest days in the gym, it's essential to allow your mind to rest during meditation. Take short breaks between sessions and consider incorporating rest days where you engage in less intense mindfulness activities like walking or gentle stretching.")
        st.write(" - **Reflect and Adjust**: Periodically assess your meditation practice. If you find that you're struggling to maintain focus during longer sessions, it may be time to reduce the duration temporarily and gradually build up again.")
# end function
    

def timer(meditation_time, break_time):
    meditation_seconds = meditation_time*60
    break_seconds = break_time*60

    # has a maximum upper limit of 100
    my_bar = st.progress(0,text="Meditate")

    # gives 100 equal parts of the seconds
    perc = meditation_seconds/100
    for i in range(100):
        my_bar.progress(i+1, text="Meditate")
        time.sleep(perc)
    # next i

    # caues that bar to dissapear when completed
    time.sleep(1)
    my_bar.empty()

    # has a maximum upper limit of 100
    my_bar = st.progress(0,text="Rest")

    # gives 100 equal parts of the seconds
    perc = break_seconds/100
    for i in range(100):
        my_bar.progress(i+1, text="Rest")
        time.sleep(perc)
    # next i

    # caues that bar to dissapear when completed
    time.sleep(1)
    my_bar.empty()
# end function
home_screen()


    