harddrive=5120
picture_size=3
video_size=15

no_pictures=int(input("please add the total number of the pictures:\n"))
no_videos=int(input("please add the total number of the videos:\n"))

total_picture_size=no_pictures*picture_size
total_video_size=no_videos*video_size

free_space=harddrive-total_picture_size-total_video_size
if free_space <0:
    print("Not Enough Space")
else:
    print(free_space)