from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt= YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video download successful!")
    except Exception as e:
        print('an error occured: ', e)

url = "https://www.youtube.com/watch?v=lsMQRaeKNDk&t=170s"
save_path = r"C:\Users\yance\OneDrive\Documents\DownloadedVideos"

download_video(url, save_path)