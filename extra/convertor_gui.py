import PySimpleGUI as sg

feet_label = sg.Text("Feet")
feet_input = sg.Input()
inches_label = sg.Text("Inches")
inches_input = sg.Input()
convert_button = sg.Button("Convert")

layout = [[feet_label, feet_input],
          [inches_label, inches_input],
          [convert_button]]

window = sg.Window("Convertor", layout=layout)
window.read()
window.close()
