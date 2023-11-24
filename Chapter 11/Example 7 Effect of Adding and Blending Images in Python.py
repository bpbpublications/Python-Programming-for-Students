# Demonstrating Effects of Adding and Blending Images

import cv2
import numpy as np
new_image1 = cv2.imread(r"D:\images\boat.png")
new_image2 = cv2.imread(r"D:\images\nature.png")
# Resize one image to match sizes of both images
new_image2 = np.resize(new_image2,new_image1.shape)
print(new_image1.shape, new_image2.shape)
added_image = cv2.add(new_image1, new_image2)
blended_image = cv2.addWeighted(new_image1, 0.4, new_image2, 0.6, 0)
cv2.imshow('First Image', new_image1)
cv2.imshow('Second Image', new_image2)
cv2.imshow('Added Image', added_image)
cv2.imshow('Weighted Image', blended_image)
cv2.waitKey(0)
