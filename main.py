from flask import Flask, render_template, request, redirect, send_file
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import shutil

app = Flask(__name__)

def download_and_convert_to_mp3(url):
    try:
        # Baixar o vídeo do YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video_path = video.download()

        # Obter o nome do arquivo sem extensão
        video_filename = os.path.splitext(os.path.basename(video_path))[0]

        # Converter para MP3
        audio_path = f"{video_filename}.mp3"
        video_clip = AudioFileClip(video_path)
        video_clip.write_audiofile(audio_path)

        # Caminho da pasta de downloads do usuário
        user_downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        # Mover o arquivo MP3 para a pasta de downloads do usuário
        destination_path = os.path.join(user_downloads_folder, audio_path)
        shutil.move(audio_path, destination_path)

        # Excluir o arquivo de vídeo temporário
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

    # Chamar a função de download e conversão
    audio_file_path = download_and_convert_to_mp3(url)

    if audio_file_path:
        # Se a conversão for bem-sucedida, redirecionar para a página inicial com o link de download
        print("Download e conversão para MP3 concluídos com sucesso!")
        return send_file(audio_file_path, as_attachment=True)
    else:
        # Se ocorrer um erro, redirecionar de volta para a página inicial com mensagem de erro
        return redirect('/', error="Ocorreu um erro durante o download/conversão.")

if __name__ == '__main__':
    app.run(debug=True)
