import os
import shutil
import math
import datetime
from pytube import YouTube # Need to Donwload if you don't have it [pip install git+https://github.com/ssuwani/pytube]

#botão escolher qualidade do vídeo para baixar
#botão opção mp4 ou mp3 (video ou audio apenas)
#, fileTypeString

def Translate(youtubeLinkString, filetype, resolution, filename):
    """
    Translate the link of the youtube video into the selected file type.
    """
    video = YouTube(youtubeLinkString)

    # Video Attributes
    title = video.title # Title
    nViews = video.views # Number of views
    duration = (video.length/60) # Minutes
    thumbnail = video.thumbnail_url # Thumbnail

    # Selecting stream with filters
    print(video.streams.filter(file_extension=f'{filetype}', resolution=f'{resolution}'))
    stream = video.streams.filter(file_extension=f'{filetype}', resolution=f'{resolution}')[0]
    ### PROBLEMA VIDEO BAIXA MAS NAO TEM SOM!!!
    # Download stream wih selected filename
    stream.download(filename=f"{filename}")
    print(stream.download(filename=f"{filename}"))


Translate('https://www.youtube.com/watch?v=PPQ8m8xQAs8', "mp4", "1080p", "videoNovo")