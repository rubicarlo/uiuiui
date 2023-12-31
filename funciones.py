import subprocess
import os
import datetime

processes = {}

def download_video(url, video_id):
    base_path = os.path.join(os.getcwd(), 'videos', 'TS')
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    # Obtener la ruta completa al ejecutable ffmpeg.exe
    ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
    
    process = subprocess.Popen([ffmpeg_path, '-loglevel', 'panic', '-i', url, '-c', 'copy', '-b:v', '5M', os.path.join(base_path, f'video_{video_id}.ts')])
    processes[video_id] = process

def convert_to_mp4(video_id, ffmpeg_path):
    base_path = os.path.join(os.getcwd(), 'videos')
    ts_path = os.path.join(base_path, 'TS')
    input_filename = f'video_{video_id}.ts'
    input_path = os.path.join(ts_path, input_filename)
    if not os.path.exists(input_path):
        return
    output_filename = f'video_{video_id}_{datetime.datetime.now().strftime("%d-%m-%Y")}.mp4'
    output_path = os.path.join(base_path, output_filename)
    i = 2
    while os.path.exists(output_path):
        output_filename = f'video_{video_id}_{datetime.datetime.now().strftime("%d-%m-%Y")}_{i}.mp4'
        output_path = os.path.join(base_path, output_filename)
        i += 1
    subprocess.run([ffmpeg_path, '-loglevel', 'panic', '-i', input_path, '-c', 'copy', output_path])
    os.remove(input_path)

def stop_download(video_id):
    process = processes.get(video_id)
    if process is not None:
        process.terminate()
        process.wait()
        processes[video_id] = None
        ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
        convert_to_mp4(video_id, ffmpeg_path)