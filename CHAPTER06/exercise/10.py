import numpy as np
import cv2

image1 = np.zeros((50, 512), np.float32)
rows, cols = image1.shape[:2]

print(rows, cols)
for i in range(rows):
    for j in range(cols):
        image1.itemset((i, j), j / 512)

image1 = image1[:, ::-1]
cv2.imshow("image1", image1)
cv2.waitKey(0)
