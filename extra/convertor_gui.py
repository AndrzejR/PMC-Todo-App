import PySimpleGUI as sg

feet_label = sg.Text("Feet")
feet_input = sg.Input(key='feet_input')
inches_label = sg.Text("Inches")
inches_input = sg.Input(key='inches_input')
convert_button = sg.Button("Convert")
output_label = sg.Text(key='output_label')

layout = [[feet_label, feet_input],
          [inches_label, inches_input],
          [convert_button, output_label]]

window = sg.Window("Convertor",
                   layout=layout,
                   font=('Mono', 16))

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert':
        feet = int(values['feet_input'])
        inches = int(values['inches_input'])
        result = feet * 30.48 + inches * 2.54
        window['output_label'].update(value=f"{result} cms")


window.close()
