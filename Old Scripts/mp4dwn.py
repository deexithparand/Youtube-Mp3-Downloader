import pytube

list = ["https://www.youtube.com/watch?v=CvM8DzBEFSE"]

for i in range(0,1):
	#getting data we need 
	dwn_path = "C:/Users/deexi/OneDrive/Desktop/WebDev/Pytube/Mp4Garage"
	
	yt_url = list[i]
	
	#creating file object for the module
	#creating object using url
	yt_obj = pytube.YouTube(yt_url)
	
	#name download file using the same video title
	d_filename = yt_obj.title
	
	#filter to mp4 files
	#try:
		#The streams with progressive=True are the videos that include both audio and video in the same stream. 
		#mp4file = yt_obj.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
		# "or" ♥♥♥
	mp4file = yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
	mp4file.download(output_path=dwn_path,filename=d_filename)
	#except:
	#	print("Code Error!!!")
#print("Successfull ♥♥♥")



               

