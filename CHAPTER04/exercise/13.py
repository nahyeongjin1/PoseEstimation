import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/read_color.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

cv2.imwrite("images/test.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite("images/test.png", image, (cv2.IMWRITE_PNG_COMPRESSION, 9))

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 잘 됨