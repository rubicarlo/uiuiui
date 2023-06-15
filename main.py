import os
import uuid
import funciones
import ui

# Función que maneja los eventos de la GUI
def handle_event(event, values):
    if event == 'Carpeta':
        # Abre la carpeta de videos
        os.startfile('videos')

    if event == 'Limpiar':
        ui.clear_stopped_files()

    if event == 'Descargar':
        url = values['-URL-']
        video_id = str(uuid.uuid4())

        # Llamamos a la función "download_video" del archivo "funciones.py" para descargar el video
        funciones.download_video(url, video_id)

        # Agregamos la fila de la descarga en la tabla
        row = [video_id, f"video_{video_id}.mp4", "Descargando"]
        ui.window['-TABLE'].update([*ui.window['-TABLE'].get(), row])

    if event == 'Detener descarga':
        selected_rows = ui.window['-TABLE'].SelectedRows  # Obtenemos las filas seleccionadas
        for row_index in selected_rows:
            video_data = ui.window['-TABLE'].get()[row_index]  # Obtenemos los datos de la fila seleccionada
            if video_data:
                video_id = video_data[0]

                # Llamamos a la función "stop_download" del archivo "funciones.py" para detener la descarga del video
                funciones.stop_download(video_id)

                # Actualizamos el estado de la descarga en la tabla
                ui.update_table(video_id, "Detenida")



# Bucle principal de la GUI
while True:
    event, values = ui.window.read()

    # Manejamos el evento
    handle_event(event, values)

    # Verificamos si el usuario cerró la ventana
    if event == ui.sg.WIN_CLOSED:
        break

# Cerramos la ventana al finalizar
ui.close_window()