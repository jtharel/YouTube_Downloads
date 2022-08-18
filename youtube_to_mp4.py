# Download videos from YouTube in mp4 format

from pytube import YouTube
import os

yt = YouTube(str(input("Enter YouTube Url here: ")))
video = yt.streams.get_highest_resolution()        

print("Enter the destination to save file, leave blank for current directory")
destination = str(input(": ")) or '.'
out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded in .mp4 format.")

