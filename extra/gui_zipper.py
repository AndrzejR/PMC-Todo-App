import PySimpleGUI as sg

label1 = sg.Text("Select files to zip")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

layout = [[label1, input1, choose_button1],
          [label2, input2, choose_button2],
          [compress_button]]

window = sg.Window("Zipper", layout=layout)
window.read()
window.close()
