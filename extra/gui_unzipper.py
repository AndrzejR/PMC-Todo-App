import PySimpleGUI as sg
import zipfile
import pathlib

file_to_unzip_label = sg.Text("Select file to unzip")
file_input = sg.Input(key='file_input')
choose_button1 = sg.FileBrowse("Choose")

dest_folder_label = sg.Text("Select destination folder")
folder_input = sg.Input(key='folder_input')
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("UnCompress")
output_label = sg.Text(key='output_label')

layout = [[file_to_unzip_label, file_input, choose_button1],
          [dest_folder_label, folder_input, choose_button2],
          [compress_button, output_label]]

window = sg.Window("UnZipper", layout=layout,
                   font=('Mono', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'UnCompress':
        file_to_unzip = values['file_input']
        target_folder = values['folder_input']
        target_folder = pathlib.Path(target_folder)
        with zipfile.ZipFile(file_to_unzip, 'r') as archive:
            archive.extractall(target_folder)
        window['output_label'].update(value='UnCompression completed!')

window.close()
