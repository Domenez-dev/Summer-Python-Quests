from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'downloads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_video', methods=['POST'])
def fetch_video():
    url = request.form['url']
    try:
        video = YouTube(url)
        thumbnail_url = video.thumbnail_url
        title = video.title
        streams = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
        resolutions = [stream.resolution for stream in streams]
        return render_template('details.html', thumbnail_url=thumbnail_url, title=title, resolutions=resolutions, url=url)
    except Exception as e:
        return f"Failed to fetch video: {e}"

@app.route('/download_video', methods=['POST'])
def download_video():
    url = request.form['url']
    resolution = request.form['resolution']
    format_choice = request.form['format']

    try:
        video = YouTube(url)
        if format_choice == "mp4":
            stream = video.streams.filter(res=resolution, progressive=True, file_extension='mp4').first()
        else:
            stream = video.streams.filter(only_audio=True, file_extension='mp4').first()

        download_path = app.config['UPLOAD_FOLDER']
        os.makedirs(download_path, exist_ok=True)
        stream.download(output_path=download_path)

        if format_choice == "mp3":
            base, ext = os.path.splitext(stream.default_filename)
            new_file = base + '.mp3'
            os.rename(os.path.join(download_path, stream.default_filename), os.path.join(download_path, new_file))

        return send_file(os.path.join(download_path, stream.default_filename), as_attachment=True)
    except Exception as e:
        return f"Failed to download video: {e}"

if __name__ == '__main__':
    app.run(debug=True)
