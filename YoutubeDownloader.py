from pytube import YouTube
import os

URL = "https://www.youtube.com/watch?v=CA-e5eWB7eg"
yt = YouTube(URL)

video = yt.streams.all()
vid = video[0]

s = 1
for v in video:
    print(str(s) +'.' + str(v))
    s+= 1


dest = os.path.dirname('C:\\Users\\Tyron\\Videos\\')
vid.download(dest)


## Give user option for 360p and 720p video, as well as mp3 audio