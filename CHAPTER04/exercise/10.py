import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global image, title
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), 20, (0, 0, 0))
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x-15, y-15, 30, 30), (0, 0, 0))
        cv2.imshow(title, image)


image = np.zeros((400, 400, 3), np.uint8)
image[:] = (255, 255, 255)

title = "Mouse event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
