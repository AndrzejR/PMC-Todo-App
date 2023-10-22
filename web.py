import streamlit as st
import functions

todos = functions.read_todos()

st.title("A Generic To-Do App")
st.subheader("Get stuff done.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add a todo...")
