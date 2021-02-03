# 다음과 같이 컬러 입력 영상에 허프 변환으로 직선을 구해서 표시하시오.

import numpy as np, cv2, math
from Common.hough import houghLines

def draw_houghLines(src, lines, nline):
    dst = src
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)
        delta = (-1000 * b, 1000 * a)
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)
    return dst

color_image = cv2.imread("images/11.jpg", cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray_image, (5, 5), 2, 2)
canny = cv2.Canny(blur, 50, 150, 5)

rho, theta = 1, np.pi / 180
lines = houghLines(canny, rho, theta, 80)
dst = draw_houghLines(color_image, lines, 10)

cv2.imshow("detected lines", dst)
cv2.waitKey(0)
