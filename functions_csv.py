import csv
FILEPATH = './files/todos.csv'


def read_todos():
    """
    Read the default file with todos
    and return the list of todos.
    :return: List of todos
    """
    with open(FILEPATH, 'r') as file:
        todos_from_file = list(csv.reader(file))
        for t in todos_from_file:
            print(t)
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
    Prints the todos one line per todo.
    :param todos_to_show: List of todos to show
    :return: None
    """
    for i, t in enumerate(todos_to_show):
        row = f"{i + 1}: {t.strip()}"
        print(row)

if __name__ == "__main__":
    read_todos()