import numpy as np
import cv2

image = np.zeros((600, 400, 3), np.uint8)
image[:] = (255, 255, 255)

cv2.rectangle(image, (100, 100), (300, 400), (0, 0, 255), cv2.LINE_4)


cv2.imshow("rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
