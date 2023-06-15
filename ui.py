import PySimpleGUI as sg

column_names = ['ID', 'Nombre del vídeo', 'Estado']

layout = [
    [sg.Table(values=[], headings=column_names, col_widths=[10, 500, 50], num_rows=10, auto_size_columns=True,
              justification='center', key='-TABLE', expand_x=True,expand_y=True, enable_events=True, select_mode=sg.TABLE_SELECT_MODE_EXTENDED)],
    [sg.Input(key='-URL-'), sg.Button('Descargar')],
    [sg.Button('Detener descarga'), sg.Button('Carpeta'), sg.Button('Limpiar')]
]

window = sg.Window('Descargador de videos', layout, resizable=True)

def update_table(video_id, status):
    table_values = window['-TABLE'].get()
    for i, value in enumerate(table_values):
        if value[0] == video_id:
            table_values[i][2] = status
            break
    window['-TABLE'].update(table_values)

def close_window():
    window.close()

def clear_stopped_files():
    table_values = window['-TABLE'].get()
    updated_table_values = [value for value in table_values if value[2] != "Detenida"]
    window['-TABLE'].update(updated_table_values)