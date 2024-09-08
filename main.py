from flask import Flask, render_template, request, redirect, send_file
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import shutil

app = Flask(__name__)

def download_and_convert_to_mp3(url):
    try:
       
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video_path = video.download()

       
        video_filename = os.path.splitext(os.path.basename(video_path))[0]

      
        audio_path = f"{video_filename}.mp3"
        video_clip = AudioFileClip(video_path)
        video_clip.write_audiofile(audio_path)

        user_downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
 
        destination_path = os.path.join(user_downloads_folder, audio_path)
        shutil.move(audio_path, destination_path)

      
        os.remove(video_path)

        return destination_path

    except Exception as e:
        print(f"Ocorreu um erro durante o download/conversão: {str(e)}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/baixar', methods=['POST'])
def baixar():
    url = request.form.get('url')

   
    audio_file_path = download_and_convert_to_mp3(url)

    if audio_file_path:
        
        print("Download e conversão para MP3 concluídos com sucesso!")
        return send_file(audio_file_path, as_attachment=True)
    else:
        
        return redirect('/', error="Ocorreu um erro durante o download/conversão.")

if __name__ == '__main__':
    app.run(debug=True)
