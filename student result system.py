import streamlit as st
st.title("Student Result")
name=st.text_input("student name")
name=st.text_input("Student Name")
m1=st.number_input("Python")
m2=st.number_input("java")
m3=st.number_input("DBMS")
percentage=(m1+m2+m3)/3
if st.button("Show Result"):
    st.write("student",name)
    st.write("percenatge",round(percentage,2))
    if percentage>=60:
        st.success("first division")
    elif percentage>=45:
        st.warning("second division")
    elif percentage>=33:
        st.warning("third division")
    else:
        st.error("fail")
