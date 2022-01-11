from moviepy.editor import *
import os
from config import sizes

def file_size(file_name):
    sd = 1024**2
    result = round(int(os.path.getsize(file_name))/sd, 2)
    return result

def compressor(dirname,filename, sifat):
    clip1 = VideoFileClip(f"{dirname}/{filename}.mp4")
    clip1 = clip1.resize( sizes[sifat] )
    clip1.write_videofile(f'{dirname}/{filename}{sifat}.mp4')
    return f'{dirname}/{filename}{sifat}.mp4'
    
