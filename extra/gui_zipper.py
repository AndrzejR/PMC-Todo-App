import PySimpleGUI as sg
import zipfile
import pathlib

files_to_zip_label = sg.Text("Select files to zip")
files_input = sg.Input(key='files_input')
choose_button1 = sg.FilesBrowse("Choose")

dest_folder_label = sg.Text("Select destination folder")
folder_input = sg.Input(key='folder_input')
choose_button2 = sg.FolderBrowse("Choose")

dest_file_label = sg.Text("Enter destination filename")
filename_input = sg.Input(key='filename_input')

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output_label')

layout = [[files_to_zip_label, files_input, choose_button1],
          [dest_folder_label, folder_input, choose_button2],
          [dest_file_label, filename_input],
          [compress_button, output_label]]

window = sg.Window("Zipper", layout=layout,
                   font=('Mono', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Compress':
        files_to_zip = values['files_input'].split(";")
        target_folder = values['folder_input']
        target_filename = values['filename_input']
        target_file = pathlib.Path(target_folder, target_filename)
        with zipfile.ZipFile(target_file, 'w') as archive:
            for filepath in files_to_zip:
                filepath = pathlib.Path(filepath)
                archive.write(filepath, arcname=filepath.name)
        window['output_label'].update(value='Compression completed!', text_color='green')

window.close()
