import numpy as np, cv2
from Common.interpolation import bilinear_value
from Common.functions import contain

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, [x, y])
    return dst

image = cv2.imread("images/12.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

dst = rotate(image, 30)

cv2.imshow("dst", dst)
cv2.waitKey(0)
