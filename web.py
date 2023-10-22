import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("A Generic To-Do App")
st.subheader("Get stuff done.")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add a todo...",
              on_change=add_todo, key='new_todo')
