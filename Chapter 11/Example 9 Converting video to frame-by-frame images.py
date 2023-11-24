# Converting video to frame-by-frame images

import cv2
video_file = cv2.VideoCapture(r"D:\videos\samplevideo.mp4")
frameID = 0
while(True):
   flag, frame_read = video_file.read()
   if flag == True:
      # Continue creating image frames till video ends
      framename = str(frameID) + '.png'
      print ('Next frame read...' + name)
      cv2.imwrite(framename, frame_read)
      frameID += 1
   else: break
video_file.release()
cv2.destroyAllWindows()
