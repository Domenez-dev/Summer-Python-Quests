from pytube import YouTube

def download_video(url, path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        
        # Display available resolutions
        print("Available resolutions:")
        for i, stream in enumerate(streams, start=1):
            print(f"{i}. {stream.resolution}")

        # Prompt user to select resolution
        choice = int(input("Enter the number corresponding to the desired resolution: "))
        selected_stream = streams[choice - 1]

        print(f'Downloading: {yt.title} at {selected_stream.resolution}')
        selected_stream.download(path)
        print('Download complete.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    url = input('Enter the YouTube video URL: ')
    path = input('Enter the download path: ')
    download_video(url, path)
