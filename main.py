import os
import uuid
import funciones
import ui

def handle_event(event, values):
    if event == 'Carpeta':
        os.startfile('videos')

    if event == 'Limpiar':
        ui.clear_stopped_files()

    if event == 'Descargar':
        url = values['-URL-']
        video_id = str(uuid.uuid4())

        funciones.download_video(url, video_id)

        row = [video_id, f"video_{video_id}.mp4", "Descargando"]
        ui.window['-TABLE'].update([*ui.window['-TABLE'].get(), row])

    if event == 'Detener descarga':
        selected_rows = ui.window['-TABLE'].SelectedRows  # Obtenemos las filas seleccionadas
        for row_index in selected_rows:
            video_data = ui.window['-TABLE'].get()[row_index]  # Obtenemos los datos de la fila seleccionada
            if video_data:
                video_id = video_data[0]

                funciones.stop_download(video_id)

                ui.update_table(video_id, "Fin")

while True:
    event, values = ui.window.read()

    handle_event(event, values)

    if event == ui.sg.WIN_CLOSED:
        break

ui.close_window()