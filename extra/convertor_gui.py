import PySimpleGUI as sg

sg.theme("Black")

feet_label = sg.Text("Feet")
feet_input = sg.Input(key='feet_input')
inches_label = sg.Text("Inches")
inches_input = sg.Input(key='inches_input')
convert_button = sg.Button("Convert")
output_label = sg.Text(key='output_label')

exit_button = sg.Button("Exit")

layout = [[feet_label, feet_input],
          [inches_label, inches_input],
          [convert_button, output_label],
          [exit_button]]

window = sg.Window("Convertor",
                   layout=layout,
                   font=('Mono', 16))

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == 'Convert':
        try:
            feet = int(values['feet_input'])
            inches = int(values['inches_input'])
            result = feet * 30.48 + inches * 2.54
            window['output_label'].update(value=f"{result} cms")
        except ValueError:
            sg.popup("Please provide feet and inches as two numbers")

window.close()
