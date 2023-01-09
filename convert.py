import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("video.mp4"))
video.audio.write_audiofile(os.path.join("audio.mp3))
                                         
