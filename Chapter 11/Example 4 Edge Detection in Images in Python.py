# Edge detection in Images

import cv2
import sys
# The first argument is the image
new_img = cv2.imread('D:\images\HeritageBuilding.png')
# First convert to grayscale for easy handling
gray_image = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
# Next apply Gaussian blur operation to converted image
gaussian_blurred_image = cv2.GaussianBlur(gray_image, (5,5), 0)
cv2.imshow("Blurred Image", new_img)
cv2.waitKey(0)
# Apply canny() for edge detection
apply_canny1 = cv2.Canny(gaussian_blurred_image, 10, 50)
cv2.imshow("Applied Canny with lower thresholds", apply_canny1)
cv2.waitKey(0)
apply_canny2 = cv2.Canny(gaussian_blurred_image, 60, 200)
cv2.imshow("Applied Canny with higher thresholds", apply_canny2)
cv2.waitKey(0)
