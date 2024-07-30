#requires ffmpeg -> apt install ffmpeg
#pip3 install yt_dlp

import yt_dlp
import os

def download_youtube_video():
    # Ask user for YouTube URL
    url = input("Enter the YouTube video URL: ")
    
    # Ask user for download path
    output_path = input("Enter the download path (leave empty for current directory): ")
    if not output_path:
        output_path = '.'
    
    # Ensure the download path exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Set yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4'
    }
    
    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Download complete!")

if __name__ == "__main__":
    download_youtube_video()

