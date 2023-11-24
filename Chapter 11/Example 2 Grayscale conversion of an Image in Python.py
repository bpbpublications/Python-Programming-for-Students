# Graysacale conversion of an Image

import cv2
new_img = cv2.imread(‘D:\images\HeritageBuilding.png’)
# To convert BGR image to Grayscale
convert_gray_image = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
cv2.imshow(‘Converted Gray Image’, convert_gray_image)
cv2.waitKey(0)
