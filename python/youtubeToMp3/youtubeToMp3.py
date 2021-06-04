#!/usr/bin/env python
"""
This program provides a video from Youtube to be downloaded in the local machine.

Using the pytube library for this job of translating the url of the video into mp3 and mp4 files.

"""

import os
import shutil
import math
import datetime
from pytube import YouTube # Need to Donwload if you don't have it (pip install git+https://github.com/ssuwani/pytube)

__author__ = "Rafael Seicali Malcervelli"
__maintainer__ = "Rafael Seicali Malcervelli"
__email__ = "r.malcervelli@gmail.com"

#botão escolher qualidade do vídeo para baixar
#botão opção mp4 ou mp3 (video ou audio apenas)
#nome o que quer ou default?

#Pesquisar como fazer isso
def Loading():
    """
    Loading function animation while downloading the file.
    """
    return None

def Translate(youtubeLinkString, filetype, resolution, filename):
    """
    Translate the link of the youtube video into the selected file type.

    Args:
        youtubeLinkString: Url of the youtube video that you like to download.
        filetype: 'mp3' (audio only) or 'mp4' (video and audio).
        resolution (for mp3 files, consider as 'size of file'): 'Light' => Poor image resolution but lightweight file || 'Medium' => Medium image resolution and mediumweight file || 'Better' => Best image resolution and largeweight file
        filename: Specific name of the file that will be downloaded.
    Returns:
        A file downloaded in your local machine with the selected resolution method, filetype and filename.
    """
    video = YouTube(youtubeLinkString)

    # Video Attributes
    title = video.title # Title
    nViews = video.views # Number of views
    duration = (video.length/60) # Minutes
    thumbnail = video.thumbnail_url # Thumbnail

    # Filtering filetype
    # MP3
    if filetype.casefold() == "mp3":
        # Audio only
        streamsMP3 = video.streams.filter(only_audio=True)

        if resolution.casefold() == "light":
            streamLight = streamsMP3.filter(abr="70kbps")
            if filename == "default":
                streamLight.download(filename=f"{streamLight.default_filename}")
            else:
                streamLight.download(filename=f"{filename}")

        elif resolution.casefold() == "medium":
            streamMedium = streamsMP3.filter(abr="128kbps")
            if filename == "default":
                streamMedium.download(filename=f"{streamMedium.default_filename}")
            else:
                streamMedium.download(filename=f"{filename}")
        
        elif resolution.casefold() == "better":
            streamBetter = streamsMP3.filter(abr="160kbps")
            if filename == "default":
                streamBetter.download(filename=f"{streamBetter.default_filename}")
            else:
                streamBetter.download(filename=f"{filename}")

    # MP4
    elif filetype.casefold() == "mp4":
        # Video and audio
        # Audio only
        streamsMP4 = video.streams.filter(progressive=True)

        if resolution.casefold() == "light":
            streamLight = video.streams.get_lowest_resolution()
            if filename == "default":
                streamLight.download(filename=f"{streamLight.default_filename}")
            else:
                streamLight.download(filename=f"{filename}")

        elif resolution.casefold() == "medium":
            streamMedium = streamsMP4.filter(res="480p")
            if len(streamMedium) < 0:
                streamMedium = streamsMP4.filter(res="360p")
            if filename == "default":
                streamMedium.download(filename=f"{streamMedium.default_filename}")
            else:
                streamMedium.download(filename=f"{filename}")
        
        elif resolution.casefold() == "better":
            streamBetter = video.streams.get_highest_resolution()
            if filename == "default":
                streamBetter.download(filename=f"{streamBetter.default_filename}")
            else:
                streamBetter.download(filename=f"{filename}")

    # Download stream wih selected filename
    print("[+]Downloading...")
    #stream.download(filename=f"{filename}").on_progress
    #print(stream.download(filename=f"{filename}"))

# Main function
def main():
    try:
        Translate("https://www.youtube.com/watch?v=BSzSn-PRdtI", "mp4", "360p", "beautifulMistakes")

    except Exception as erro:
        print("Error:")
        print(erro)


# Script for console running
if __name__ == "__main__":
    main()
        


