import cv2
from Common.utils import put_string


def brightness_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value)


def contrast_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)


capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)

title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar('brightness', title, 0, 100, brightness_bar)
cv2.createTrackbar('contrast', title, 0, 100, contrast_bar)

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    brightness = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    contrast = int(capture.get(cv2.CAP_PROP_CONTRAST))
    put_string(frame, 'brightness : ', (10, 240), brightness)
    put_string(frame, 'contrast : ', (10, 270), contrast)
    cv2.imshow(title, frame)

capture.release()

# 잘 됨
