#mp3 converter
from moviepy.editor import *

# FILE NAMES ------------ 

mp4FileName = "Aarambam Theme Music in arivu.mp4" 

mp3FileName = mp4FileName[:-4] + ".mp3"

# EDITING ------------

#videoClip = VideoFileClip(mp4FileName).path("C:/Users/deexi/OneDrive/Desktop/WebDev/Pytube/Mp4Garage/Aarambam Theme Music in arivu.mp4")

videoClip = VideoFileClip(mp4FileName)

audioClip = videoClip.audio

audioClip.write_audiofile(mp3FileName)

audioClip.close()

videoClip.close()

print("Operation Success ♥♥♥♥")
