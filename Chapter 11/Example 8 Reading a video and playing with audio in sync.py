# Reading a video and playing with audio in sync

import cv2
from ffpyplayer.player import MediaPlayer
video_file = r"D:\videos\samplevideo.mp4"
video_read = cv2.VideoCapture(video_file)
player = MediaPlayer(video_file)
while True:
   flag, frame_read = video_read.read()
   audio_frame, value = player.get_frame()
   if not flag:
      print("End of video")
      break
   if cv2.waitKey(1) == ord("q"):
      break
   cv2.imshow("Video", frame_read)
   if value != 'eof' and audio_frame is not None:
      image, time = audio_frame
video_read.release()
cv2.destroyAllWindows()
