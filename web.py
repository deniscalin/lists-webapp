import streamlit
import functions
from PIL import Image

todos = functions.get_todos()


def add_todo():
    todo = streamlit.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write(todos)


streamlit.title("Nulist Idea Mapping Service")
streamlit.subheader("Control your day! Add todo.")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()


streamlit.text_input(label="Enter your todo", placeholder="Add todo", on_change=add_todo,
              key="new_todo")


image = Image.open('nulist_logo_n.png')
#streamlit.image(image, width=100)

col1, col2, col3 = streamlit.columns([0.2, 5, 0.5])
col3.image(image, use_column_width=True)
