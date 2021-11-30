#Mp4 to Mp3 converter
from moviepy.editor import *

list = ["Aarambam Theme Music in arivu.mp4"]

#try:
for i in range(0,1):
	#len(list)
	#mp4_file = "ccv_song.mp4"
	mp4_file = list[i]
		
	file_d = str(i+1)+".mp3"

	mp3_file = file_d
		
	videoClip = VideoFileClip(mp4_file).path("C:/Users/deexi/OneDrive/Desktop/WebDev/Pytube/Mp4Garage")
		
	audioClip = videoClip.audio
		
	audioClip.write_audiofile(mp3_file)
		
	audioClip.close()
		
	videoClip.close()

#except:
#	print("Some error has occured!!")

print("Successful ♥♥♥♥")