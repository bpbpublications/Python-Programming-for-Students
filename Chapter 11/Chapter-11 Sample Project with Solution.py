# Sample project with solution
# Create an application for Face Detection in an image. Along with that, once a face is detected, 
# then we try to locate and highlight eyes in the face. Furthermore, the application detects a smile on the face and
# draws a boundary to highlight the smile as well. Also, the program counts and displays the total number of faces detected in an image.
# The OpenCV library uses haarcascades XML files as filters to make the detections related to a face and various parts of it 
# like eyes and smile. The GitHub link for these files is opencv/data/haarcascades at master · opencv/opencv · GitHub

# Solution

import cv2
# Import xml files for face detection and eye detection
face_cascade_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade_file = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade_file = cv2.CascadeClassifier('haarcascade_smile.xml')
image_file = cv2.imread(r'D:\images\movie.png')
# convert to gray scale of each frames
grayscale_image = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
# Detects faces of different sizes in the input image
# The detectMultiScale() detects different size faces in input image and returns rectangles positioned on the faces.
# The first parameter is the input image, the second one is scale factor which defines the reduction size of image
# and the third argument is the minNeighbors i.e. neighbors each rectangle must have.The scaleFactor=1.3 and minNeighbors=5 are chosen on experimental basis.
faces_detect = face_cascade_file.detectMultiScale(grayscale_image, scaleFactor = 1.3, minNeighbors = 5)
# Define loop for each face detected utilizing generated coordinates in above function
for (x,y,w,h) in faces_detect:
   # Next draw a rectangle in the input image. Here (255,0,0) is the color of the frame in RGB. # The last parameter value 2 denotes the thickness of the rectangle. Here x refers to the initial horizontal position,
   # w refers to the width, the vertical initial position denoted by y and h denotes height.
   image_rect =cv2.rectangle(image_file,(x,y),(x+w,y+h),(255,0,0),2)
   # Next define roi_gray_img as the region of major interest i.e. face area to look for the eyes.
   roi_gray_img = grayscale_image[y:y+h, x:x+w]
   # Now set the same region of interest in the original imageframe.
   roi_color_img = image_rect[y:y+h, x:x+w]
   # Now apply same function to detect eyes and draw rectangles
   eyes_detect = eye_cascade_file.detectMultiScale(roi_gray_img)
   for (ex,ey,ew,eh) in eyes_detect:
      cv2.rectangle(roi_color_img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
   # Further apply detectMultiScale() function to detect smile and draw rectangles
   smiles_detect = smile_cascade_file.detectMultiScale(roi_gray_img, 1.1, 22)
   for (sx, sy, sw, sh) in smiles_detect:
      cv2.rectangle(roi_color_img, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
 print("There are {0}faces in the image".format(len(faces_detect)))
 cv2.imshow('Face and Eye Detected Image',image_file)
cv2.waitKey(0)
cv2.destroyAllWindows()
