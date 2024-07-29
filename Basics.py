# app.py
import streamlit as st

def page_1():
    st.write("Welcome to Page 1")

def page_2():
    st.write("Welcome to Page 2")

page = st.sidebar.selectbox("Choose a page", ["Page 1", "Page 2"])

if page == "Page 1":
    page_1()
else:
    page_2()
