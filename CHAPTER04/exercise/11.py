import numpy as np
import cv2


def thicknessChange(value):
    global image, center, radius, thickness
    thickness = value
    image = np.zeros((400, 400, 3), np.uint8)
    image[:] = (255, 255, 255)
    cv2.circle(image, center, radius, (0, 0, 0), thickness)
    cv2.imshow(title, image)


def radiusChange(value):
    global image, center, radius, thickness
    radius = value
    image = np.zeros((400, 400, 3), np.uint8)
    image[:] = (255, 255, 255)
    cv2.circle(image, center, radius, (0, 0, 0), thickness)
    cv2.imshow(title, image)


center = (200, 200)
radius = 1
thickness = 1
image = np.zeros((400, 400, 3), np.uint8)
image[:] = (255, 255, 255)

title = "Circle"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.createTrackbar("thickness", title, thickness, 10, thicknessChange)
cv2.createTrackbar("radius", title, radius, 50, radiusChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
