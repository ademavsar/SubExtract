import tkinter as tk
from tkinter import filedialog
import subprocess

def select_videos():
    global video_paths
    video_paths = filedialog.askopenfilenames(filetypes=[("Video files", "*.mkv *.mp4")])
    videos_label.config(text=f'{len(video_paths)} video dosyası seçildi.')

def extract_subtitles():
    for video_path in video_paths:
        output_file = video_path.rsplit('.', 1)[0] + '.srt'
        command = f'ffmpeg -i "{video_path}" -map 0:s:0 -c:s copy "{output_file}"'
        subprocess.run(command, shell=True)
    result_label.config(text=f'{len(video_paths)} video dosyasından altyazı çıkarıldı.')

app = tk.Tk()
app.title('FFmpeg Toplu Altyazı Çıkarıcı')
app.geometry('400x200')  # Pencere genişliği 400px olarak ayarlandı.

video_paths = []

videos_button = tk.Button(app, text='Videoları Seç', command=select_videos)
videos_button.pack(pady=10)

videos_label = tk.Label(app, text='Henüz video seçilmedi.')
videos_label.pack(pady=5)

extract_button = tk.Button(app, text='Altyazıları Çıkar', command=extract_subtitles)
extract_button.pack(pady=10)

result_label = tk.Label(app, text='Henüz bir işlem yapılmadı.')
result_label.pack(pady=5)

app.mainloop()
