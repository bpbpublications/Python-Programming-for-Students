# Image Scaling and Rotation

import cv2
new_img = cv2.imread('D:\images\HeritageBuilding.png')
cv2.imshow('Original Image',new_img)
img_height, img_width = new_img.shape[:2]
resize_img = cv2.resize(new_img,(int(img_width/2), int(img_height/2)), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaled Image',resize_img)
img_center = (img_width / 2, img_height / 2)
rotate_matrix = cv2.getRotationMatrix2D(img_center, 90, -1)
rotated_img = cv2.warpAffine(new_img, rotate_matrix, (img_height, img_width))
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
