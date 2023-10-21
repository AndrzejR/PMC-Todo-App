import PySimpleGUI as sg
import zipfile
import pathlib

FONT = ('Mono', 14)
BUTTON_FONT = ('Mono', 11)

files_to_zip_label = sg.Text("Select files to zip")
files_input = sg.Input(key='files_input')
choose_button1 = sg.FilesBrowse("Choose files", font=BUTTON_FONT, target='files_input')

dest_folder_label = sg.Text("Select destination folder")
folder_input = sg.Input(key='folder_input')
choose_button2 = sg.FolderBrowse("Choose folder", font=BUTTON_FONT, target='folder_input')

dest_file_label = sg.Text("Enter destination filename")
filename_input = sg.Input(key='filename_input')

compress_button = sg.Button("Compress")
output_label = sg.Text(key='output_label')

col1 = sg.Column([[files_to_zip_label], [dest_folder_label], [dest_file_label]])
col2 = sg.Column([[files_input], [folder_input], [filename_input]])
col3 = sg.Column([[choose_button1], [choose_button2]])

layout = [[col1, col2, col3],
          [compress_button, output_label]]

window = sg.Window("Zipper", layout=layout,
                   font=FONT)

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
