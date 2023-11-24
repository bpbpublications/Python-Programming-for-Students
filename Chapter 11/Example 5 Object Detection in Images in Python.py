# Object Detection in Images

import cv2
# Read the image
new_img = cv2.imread('D:\images\coins.png')
# First convert image to grayscale format
grayscale_image = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
# Use any blurring method to modify image
blur_img = cv2.GaussianBlur(grayscale_image, (11,11), 0)
# Apply Canny edge detector
apply_canny = cv2.Canny(blur_img, 150, 250)
# Use findContours() to find out the contour edges and draw them
contours, hierarchy= cv2.findContours(apply_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(new_img, contours, -1, (0,255,0), 2)
cv2.imshow("Detecting Objects", new_img)
print("Number of objects found = ", len(contours))
cv2.waitKey(0)
