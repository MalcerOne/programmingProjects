#!/usr/bin/env python
"""
This program provides a video from Youtube to be downloaded in the local machine.

Using the pytube library for this job of translating the url of the video into mp3 and mp4 files.
"""

# Import necessary modules
import os, sys, shutil, math, datetime, platform
import shutil
import math
import datetime
from pytube import YouTube # Need to Donwload if you don't have it (pip install git+https://github.com/ssuwani/pytube)
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_splash_screen import Ui_SplashScreen #Splash Screen
from ui_main import Ui_MainWindow #Main windows

# Infos about the program
__author__ = "Rafael Seicali Malcervelli"
__maintainer__ = "Rafael Seicali Malcervelli"
__email__ = "r.malcervelli@gmail.com"

# Globals
counter = 0

# Function to translate the url to file
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

# Main
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelLoadingDownload.setText("<strong>Set</strong> parameters and then click on submit!")

    def downloadFile(self):
        # Light file
        if self.ui.checkBoxLight.isChecked:
            self.ui.pushButtonSubmit.clicked.connect(Translate(self.ui.textEditUrlYoutube.__str__, self.ui.spinBoxFileType.__str__, "light", self.ui.textEditFileName))

        # Medium file
        elif self.ui.checkBoxMedium.isChecked:
            self.ui.pushButtonSubmit.clicked.connect(Translate(self.ui.textEditUrlYoutube.__str__, self.ui.spinBoxFileType.__str__, "medium", self.ui.textEditFileName))

        # Better file
        elif self.ui.checkBoxBetter.isChecked:
            self.ui.pushButtonSubmit.clicked.connect(Translate(self.ui.textEditUrlYoutube.__str__, self.ui.spinBoxFileType.__str__, "better", self.ui.textEditFileName))
    

# Splash screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI - Interface codes

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTimer - start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35) # Timer in miliseconds

        # Changing description
        # Initial Text
        self.ui.label_description.setText("<strong>Welcome</strong> to my application!")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>Loading</strong> database"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>Loading</strong> user interface"))

        self.show()

    # Functions
    def progress(self):
        global counter

        # Set value of progress bar
        self.ui.progressBar.setValue(counter)

        # Close splash screen and open application
        if counter > 100:
            # Stop timer
            self.timer.stop()

            # Show main window
            self.main = MainWindow()
            self.main.show()

            # Close splash screen
            self.close()

        # Increase counter
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    print("oi2")
    # app.downloadFile()
    sys.exit(app.exec_())
    