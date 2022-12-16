import streamlit
import functions
from PIL import Image

todos = functions.get_todos()

streamlit.set_page_config(page_title="Nulist Idea Mapping Service")


def add_todo():
    todo = streamlit.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write(todos)


streamlit.title("Nulist Idea Mapping Service")
#streamlit.subheader("Control your day! Add todo.")
streamlit.write("<h2> Control your day! Add a <FONT COLOR='0076BA'>t</FONT><FONT COLOR='970E53'>o</FONT><FONT COLOR='F27200'>d</FONT><FONT COLOR='004D80'>o</FONT><FONT COLOR='017100'>.</FONT></h2>",
                unsafe_allow_html=True)

streamlit.text_input(label="Enter your todo", placeholder="Add todo", on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

image = Image.open('nulist_logo_n.png')
#streamlit.image(image, width=100)

col1, col2, col3 = streamlit.columns([0.2, 5, 0.5])
col3.image(image, use_column_width=True)
