import numpy as np, math, cv2
from Common.interpolation import bilinear_value, affine_transform
from Common.functions import contain

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = math.sin(radian), math.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, (x, y))
    return dst

image = cv2.imread("images/11.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

center = (100, 100)
angle, scale = 30, 1
size = image.shape[::-1]

dst1 = rotate_pt(image, angle, center)

rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
dst2 = cv2.warpAffine(image, rot_mat, image.shape[::-1], cv2.INTER_LINEAR)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
