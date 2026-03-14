import streamlit as st
import pandas as pd
file_path="cssforcode.css"
with open(file_path) as p:
    st.html(f"<style>{p.read()}</style>")
if "k" not in st.session_state:
    st.session_state.k=0
a=" ABCDEFGHIJ"
st.header("After completing the Selection process click ok")
if st.button("ok"):
    if a[st.session_state.k]!=' ':
        st.header("It Is Correct")
        st.header(a[st.session_state.k])
    if a[st.session_state.k]==' ':
        st.header("Please Select Atleast one Section")
c=st.sidebar.selectbox("",["select section","one","two","three","four"])
if c=="one":
    d=st.selectbox("",["select","Yes","No"])
    st.markdown("A")
    st.markdown("E")
    st.markdown("F")
    st.markdown("H")
    st.markdown("J")
    if d=="Yes":
        st.session_state.k+=1
        st.success("Done,Go Another Section")
    elif d=="No":
        st.success("Done,Go Another Section")
if c=="two":
    d=st.selectbox("",["select","YES","NO"])
    st.markdown("B")
    st.markdown("F")
    st.markdown("H")
    st.markdown("I")
    st.markdown("J")
    if d=="YES":
        st.session_state.k+=2
        st.success("Done,Go Another Section")
    elif d=="NO":
        st.success("Done,Go Another Section")
if c=="three":
    d=st.selectbox("",["select","Yes","No"])
    st.markdown("C")
    st.markdown("F")
    st.markdown("G")
    st.markdown("I")
    st.markdown("J")
    if d=="Yes":
        st.session_state.k+=3
        st.success("Done,Go Another Section")
    elif d=="No":
        st.success("Done,Go Another Section")
if c=="four":
    d=st.selectbox("",["select","YES","NO"])
    st.markdown(" D")
    st.markdown("E")
    st.markdown("G")
    st.markdown("H")
    st.markdown("I")
    st.markdown("J")
    if d=="YES":
        st.session_state.k+=4
        st.success("Done,Go Another Section")
    elif d=="NO":
        st.success("Done,Go Another Section")



