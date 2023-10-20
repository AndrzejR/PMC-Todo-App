FILEPATH = './files/todos.txt'


def read_todos():
    """
    Read the default file with todos
    and return the list of todos.
    :return: List of todos
    """
    with open(FILEPATH, 'r') as file:
        todos_from_file = [s.strip() for s in file.readlines()]
    return todos_from_file


def write_todos(todos_to_write):
    """
    Write a list of todos to the default file.
    :param todos_to_write: List of todos to save
    :return: None
    """
    with open(FILEPATH, 'w') as file:
        file.writelines(f"{s}\n" for s in todos_to_write)


def show_todos(todos_to_show):
    """
    Prints the todos one line per to-do.
    :param todos_to_show: List of todos to show
    :return: None
    """
    for i, t in enumerate(todos_to_show):
        row = f"{i + 1}: {t.strip()}"
        print(row)
