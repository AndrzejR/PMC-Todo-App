import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
todo_input = sg.InputText(tooltip="Enter to-do", key="todo_input")
add_button = sg.Button("Add")
todos_list = sg.Listbox(values=functions.read_todos(), key="todos_list",
                        enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

layout = [[todos_list], [label, todo_input, add_button, edit_button]]

window = sg.Window("A Generic To-Do App",
                   layout=layout,
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.read_todos()
        todos.append(values["todo_input"])
        functions.write_todos(todos)
        window['todos_list'].update(values=todos)
    elif event == "Edit":
        todos = functions.read_todos()
        edit_todo = values["todos_list"][0]
        todos[todos.index(edit_todo)] = values["todo_input"]
        functions.write_todos(todos)
        window['todos_list'].update(values=todos)
    elif event == "todos_list":
        todo_text = values['todos_list'][0]
        window['todo_input'].update(value=todo_text)
    elif event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()