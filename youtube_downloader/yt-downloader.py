import os
import io
import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
from threading import Thread
from PIL import Image, ImageTk
import requests

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("500x400")
        
        self.url_label = tk.Label(root, text="YouTube URL:")
        self.url_label.pack()
        
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()
        
        self.path_label = tk.Label(root, text="Download Path:")
        self.path_label.pack()
        
        self.path_entry = tk.Entry(root, width=50)
        self.path_entry.pack()
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse)
        self.browse_button.pack()
        
        self.fetch_button = tk.Button(root, text="Fetch Video", command=self.fetch_video)
        self.fetch_button.pack()
        
        self.info_frame = tk.Frame(root)
        self.info_frame.pack()
        
        self.res_label = tk.Label(self.info_frame, text="")
        self.res_label.pack()
        
        self.thumbnail_label = tk.Label(self.info_frame)
        self.thumbnail_label.pack()
        
        self.format_label = tk.Label(self.info_frame, text="Select Format:")
        self.format_label.pack()
        
        self.format_var = tk.StringVar(value="mp4")
        self.format_mp4 = tk.Radiobutton(self.info_frame, text="MP4", variable=self.format_var, value="mp4")
        self.format_mp4.pack()
        self.format_mp3 = tk.Radiobutton(self.info_frame, text="MP3", variable=self.format_var, value="mp3")
        self.format_mp3.pack()
        
        self.quality_label = tk.Label(self.info_frame, text="Select Quality:")
        self.quality_label.pack()
        
        self.quality_var = tk.StringVar(value="highest")
        self.quality_options = tk.Listbox(self.info_frame, selectmode=tk.SINGLE)
        self.quality_options.pack()
        
        self.download_button = tk.Button(root, text="Download", command=self.download_video)
        self.download_button.pack()
        
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack()
        
        self.video = None

    def browse(self):
        download_path = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, download_path)

    def fetch_video(self):
        url = self.url_entry.get()
        try:
            self.video = YouTube(url)
            self.res_label.config(text=f"Title: {self.video.title}")
            thumbnail_url = self.video.thumbnail_url
            self.show_thumbnail(thumbnail_url)
            
            self.quality_options.delete(0, tk.END)
            streams = self.video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
            for stream in streams:
                self.quality_options.insert(tk.END, stream.resolution)
            
            self.quality_options.selection_set(0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch video: {e}")
    
    def show_thumbnail(self, url):
        response = requests.get(url)
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        self.thumbnail_label.config(image=img)
        self.thumbnail_label.image = img
    
    def download_video(self):
        if self.video is None:
            messagebox.showerror("Error", "Please fetch video details first.")
            return
        
        path = self.path_entry.get()
        if not os.path.exists(path):
            messagebox.showerror("Error", "Invalid download path.")
            return

        resolution = self.quality_options.get(self.quality_options.curselection())
        format_choice = self.format_var.get()
        Thread(target=self.download_thread, args=(path, resolution, format_choice)).start()
    
    def download_thread(self, path, resolution, format_choice):
        try:
            if format_choice == "mp4":
                stream = self.video.streams.filter(res=resolution, progressive=True, file_extension='mp4').first()
            else:
                stream = self.video.streams.filter(only_audio=True, file_extension='mp4').first()
            
            self.progress_label.config(text="Downloading...")
            stream.download(output_path=path)
            if format_choice == "mp3":
                base, ext = os.path.splitext(stream.default_filename)
                new_file = base + '.mp3'
                os.rename(os.path.join(path, stream.default_filename), os.path.join(path, new_file))
            
            self.progress_label.config(text="Download complete.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")
            self.progress_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
