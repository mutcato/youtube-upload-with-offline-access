import upload_video as upload_video


video1 = {'file':'tempvideo/sample.mp4', 'title':'Sample title', 'description':'Description', 'category':'22', 'keywords':'dance,bird', 'privacy':'public'}
video2 = {'file':'tempvideo/sample2.mp4', 'title':'Sample2 title2', 'description':'Description2', 'category':'22', 'keywords':'dance,bird', 'privacy':'public'}
videos = []
videos.append(video1)
videos.append(video2)

for video in videos:
	upload_video.uploadvideo(video['file'], video['title'], video['description'], video['category'], video['keywords'], video['privacy'])