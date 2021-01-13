import numpy as np
import cv2

image1 = np.zeros((200, 300), np.uint8)
image2 = np.zeros((200, 300), np.uint8)

title1 = "win mode1"
title2 = "win mode2"
cv2.namedWindow(title1)
cv2.moveWindow(title1, 0, 0)
cv2.imshow(title1, image1)
cv2.namedWindow(title2)
cv2.moveWindow(title2, 300, 200)
cv2.imshow(title2, image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

