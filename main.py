import time

from functions import read_todos, write_todos, show_todos

while True:
    todos = read_todos()
    print("It is", time.strftime("%Y-%m-%d %H:%M:%S"))
    show_todos(todos)
    user_action = input("Type add, edit, complete or exit: ").strip()
    match user_action.split(" ")[0]:
        case "add":
            if user_action[4:]:
                todo = user_action[4:]
            else:
                todo = input("Enter a new todo: ")
            todos.append(todo)
            write_todos(todos)
        case "edit":
            try:
                if user_action[5:]:
                    number = int(user_action[5:])
                else:
                    number = int(input("Enter the number of the todo to edit: "))
                print(f"Todo number {number} is {todos[number - 1]}")
                new_todo = input("Enter a new todo: ")
                todos[number - 1] = new_todo
                write_todos(todos)
            except (ValueError, IndexError):
                print("edit must be followed by a valid number of the todo to edit")
        case "complete":
            try:
                if user_action[9:]:
                    number = int(user_action[9:])
                else:
                    number = int(input("Enter the number of the todo to complete: "))
                done_todo = todos.pop(number - 1)
                write_todos(todos)
                print(f"{done_todo} completed!")
            except (ValueError, IndexError):
                print("complete must be followed by a valid number of the todo to complete")
        case "exit":
            print("Bye!")
            break
        case _:
            print("You entered an unknown command.")
