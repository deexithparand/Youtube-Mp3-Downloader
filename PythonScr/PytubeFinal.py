#Add time cut only
import pytube
import os
from moviepy.editor import *

#dwnPath = "C:/Users/deexi/OneDrive/Desktop/WebDev/Pytube/Mp4Garage","wb"

urlLink = "https://www.youtube.com/watch?v=Un0VUHq2MZ0"

youtubeObj = pytube.YouTube(urlLink)

fileNameMp4 = youtubeObj.title 

fileMp4 = youtubeObj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

#fileMp4.download(output_path=dwnPath, filename=fileNameMp4)

fileMp4.download()

print("Download Done ♥♥♥\n")

firstWordTitle = fileNameMp4.split(" ",1)

renameName = firstWordTitle[0]+".mp4"

os.rename(fileMp4.default_filename,renameName)

#conversion --------

mp4FileName = renameName 

mp3FileName = mp4FileName[:-4] + ".mp3"

# EDITING MP3 ------------

#videoClip = VideoFileClip(mp4FileName).path("C:/Users/deexi/OneDrive/Desktop/WebDev/Pytube/Mp3Garage")

videoClip = VideoFileClip(mp4FileName)

audioClip = videoClip.audio

audioClip.write_audiofile(mp3FileName)

audioClip.close()

videoClip.close()

print("Mp3 Extracted ♥♥♥")

#deleting Mp4 file ----------

if os.path.exists(renameName):
	os.remove(renameName)
else:
	print("The file does not exist")

