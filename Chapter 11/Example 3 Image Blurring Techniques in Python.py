# Various Image Blurring techniques in python

import cv2
new_img = cv2.imread('D:\images\HeritageBuilding.png')
cv2.imshow('Original Image', new_img)
cv2.waitKey(0)
Average_blur = cv2.blur(new_img,(10,10))  # Applying Average Blur
cv2.imshow('Average Blurring', Average_blur)
cv2.waitKey(0)
Gaussian = cv2.GaussianBlur(new_img,(11,11),0) # Apply Gaussian Blur
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)
median = cv2.medianBlur(new_img, 9) # Applying Median Blur
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)
bilateral = cv2.bilateralFilter(new_img,11,70,70) # Bilateral Blur
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
