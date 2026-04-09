import streamlit as st
import numpy as np
if "a" not in st.session_state:
    st.session_state.a=np.random.randint(1,100)
    st.session_state.c=0
st.title(f"🎯Deeksha Guess the Number 🎮 !!! 🔢")
file_path="Number_Guessing_Game/Number.css"
with open(file_path) as p:
    st.html(f"<style>{p.read()}</style>")
b=st.number_input("",placeholder="Enter your Guess 🎯",value=None,step=1)
if st.button("Submit"):
    st.session_state.c+=1
    if b<st.session_state.a:
        st.warning("⬇️ Too Low 📉")
    elif b>st.session_state.a:
        st.warning("⬆️ Too high 📈")
    else:
        st.success(f"✅ done!,You win 🎉 ,number : {st.session_state.a}")
        st.success(f"You guessed in {st.session_state.c} attempts")
