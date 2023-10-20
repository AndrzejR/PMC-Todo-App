import time

from functions import read_todos, write_todos, show_todos


def main():
    while True:
        todos = read_todos()
        print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S"))
        show_todos(todos)

        user_action = input("Enter a command (add, edit, complete, exit): ").strip()
        action, *args = user_action.split(" ")

        if action == "add":
            todo = args[0] if args else input("Enter a new todo: ")
            todos.append(todo)
            write_todos(todos)
        elif action == "edit":
            try:
                number = int(args[0]) if args else int(input("Enter todo number to edit: "))
                todo = todos[number - 1]
                print(f"Editing todo #{number}: {todo}")
                new_todo = input("Enter new todo: ")
                todos[number - 1] = new_todo
                write_todos(todos)
            except (ValueError, IndexError):
                print("Invalid todo number.")
        elif action == "complete":
            try:
                number = int(args[0]) if args else int(input("Enter todo number to complete: "))
                done_todo = todos.pop(number - 1)
                write_todos(todos)
                print(f"Completed: {done_todo}")
            except (ValueError, IndexError):
                print("Invalid todo number.")
        elif action == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
