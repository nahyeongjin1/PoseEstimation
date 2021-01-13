import numpy as np
import cv2

image = np.ones((400, 600, 3), np.uint8) * 255
radius = 100
red, blue = (0, 0, 255), (255, 0, 0)

cv2.ellipse(image, (300, 200), (radius, radius), 0, 0, -180, red, -1)
cv2.ellipse(image, (300, 200), (radius, radius), 0, 0, 180, blue, -1)
cv2.ellipse(image, (250, 200), (radius//2, radius//2), 0, 0, 180, red, -1)
cv2.ellipse(image, (350, 200), (radius//2, radius//2), 0, 0, -180, blue, -1)

cv2.imshow("18", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 개 잘함 ㄷㄷ
