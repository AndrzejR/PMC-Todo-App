import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
todo_input = sg.InputText(tooltip="Enter to-do", key="todo_input")
add_button = sg.Button("Add")

exit_button = sg.Button("Exit")

layout = [[label, todo_input, add_button], [exit_button]]

window = sg.Window("A Generic To-Do App",
                   layout=layout,
                   font=('Helvetica', 13))

todos = functions.read_todos()

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos.append(values.get("todo_input"))
        functions.write_todos(todos)
    elif event == "Exit" or event == sg.WIN_CLOSED:
        functions.write_todos(todos)
        break

window.close()