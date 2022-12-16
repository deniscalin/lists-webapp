FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ A function that reads a file,
    and returns a list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write(todos_arg, filepath=FILEPATH):
    """A function that writes a to-do list object
    into a file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
