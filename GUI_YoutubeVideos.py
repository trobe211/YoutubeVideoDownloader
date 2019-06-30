import PySimpleGUI as sg
from pytube import YouTube
import os

# Layout of the window
layout = [
         [sg.Text('', size=(10, 2), font=("Helvetica", 14)), sg.Image(filename="youtube.png")],
          [sg.Text('Please enter a URL and folder')],
          [sg.Text('Video URL', size=(15, 1)), sg.InputText('')],
          [sg.Text('Folder', size=(15, 1)), sg.InputText('')],
          [sg.Text('Type', size=(15, 1)), sg.InputCombo(('720p', '360p', 'Audio'), size=(5, 1))],
          [sg.Button('Download'), sg.Cancel()]
         ]

window = sg.Window('Youtube Video Downloader').Layout(layout)

while True:

    button, values = window.Read() # Reads values and returns a dictionary
    if button is None or button == 'Cancel': # Check if the program should still run
        break

    URL = values[1]
    yt = YouTube(URL)

    video = yt.streams.all()

    if values[3] == '720p':
        vid = video[0]
    elif values[3] == '360p':
        vid = video[2]
    elif values[3] == 'Audio':
        vid = video[15]

    dest = os.path.dirname(values[2])
    vid.download(dest)
