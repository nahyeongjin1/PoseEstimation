import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(logo)

blue_img = np.zeros((blue.shape(), 3), np.uint8)
green_img = np.zeros((green.shape(), 3), np.uint8)
red_img = np.zeros((red.shape(), 3), np.uint8)

blue_img
cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue)
# cv2.imshow("green_img", green_img)
# cv2.imshow("red_img", red_img)
cv2.waitKey(0)
