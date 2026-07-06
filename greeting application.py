import streamlit as st
st.title("Welcome App")
name=st.text_input("enter your name")
if st.button("submit"):
    st.success("welcome"+name)
    
