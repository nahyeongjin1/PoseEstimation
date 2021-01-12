import numpy as np
import cv2

image = cv2.imread("images/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

min_val, max_val, a, b = cv2.minMaxLoc(image)

ratio = 255 / (max_val - min_val)
dst = np.round((image - min_val) * ratio).astype('uint8')
min_dst, max_dst, c, d = cv2.minMaxLoc(dst)

print("원본 영상 최솟값= %d, 최댓값= %d" % (min_val, max_val))
print("원본 영상 최솟값= %d, 최댓값= %d" % (min_dst, max_dst))
cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)
