# PC 카메라에서 입력받은 영상에서 허프 변환을 수행해서 최대 5개의 직선을 검출하도록 프로그램을 작성하시오.

import numpy as np, cv2
from Common.hough import houghLines, draw_houghLines

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("카메라 연결 안됨")
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)
print("카메라 연결 완료")

ret, frame = capture.read()

blur = cv2.GaussianBlur(frame, (5, 5), 2, 2)
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1, np.pi / 180
lines = houghLines(canny, rho, theta, 80)
dst = draw_houghLines(canny, lines, 7)

cv2.imshow("image", frame)
cv2.imshow("canny", canny)
cv2.imshow("dst", dst)
cv2.waitKey(0)