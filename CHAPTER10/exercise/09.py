# 허프 변환의 수행 과정에서 직선 누적 행렬을 pickle 모듈로 저장하시오.

import numpy as np, cv2, pickle
from Common.hough import accumulate, masking, select_lines, draw_houghLines

def houghLines(src, rho, theta, thresh):
    acc_mat = accumulate(src, rho, theta)
    acc_dst = masking(acc_mat, 7, 3, thresh)
    with open('data.pickle', 'wb') as f:
        pickle.dump(acc_dst, f, pickle.HIGHEST_PROTOCOL)
    lines = select_lines(acc_dst, rho, theta, thresh)
    return lines

image = cv2.imread("images/09.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

blur = cv2.GaussianBlur(image, (5, 5), 2, 2)
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1, np.pi / 180
lines = houghLines(canny, rho, theta, 80)
dst = draw_houghLines(canny, lines, 7)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("detected lines", dst)
cv2.waitKey(0)
