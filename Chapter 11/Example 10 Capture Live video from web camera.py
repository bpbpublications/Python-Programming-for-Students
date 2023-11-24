# Capture Live video from web camera

import cv2
newfile = cv2.VideoWriter('D:\video\MyVideo.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 15, (720, 560))
# To define a video capture object for built-in webcam
video_read = cv2.VideoCapture(0)
while (True):
    flag, frame_read = video_read.read()  # To capture frame by frame video
    cv2.imshow('frame', frame_read)  # To view the resultant frame
    newfile.write(frame_read)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the video capture and video write objects
video_read.release()
newfile.release()
cv2.destroyAllWindows()
