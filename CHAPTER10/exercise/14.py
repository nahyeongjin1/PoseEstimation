# 세로 방향으로 드래그할 때에도 영상 왜곡을 수행하도록 morphing() 함수의 소스를 수정하시오.

import numpy as np, cv2

def morphing1():
    h, w = image.shape[:2]
    dst = np.zeros((h, w), image.dtype)
    ys = np.arange(0, image.shape[0], 1)
    xs = np.arange(0, image.shape[1], 0.1)

    x1, x10 = pt1[0], pt1[0]*10
    ratios = xs /x1
    ratios[x10:] = (w - xs[x10:]) / (w - x1)

    dxs = xs + ratios * (pt2[0] - pt1[0])
    xs, dxs = xs.astype(int), dxs.astype(int)

    ym, xm = np.meshgrid(ys, xs)
    a, dxm = np.meshgrid(ys, dxs)
    dst[ym, dxm] = image[ym, xm]
    cv2.imshow("image", dst)

def morphing2():
    h, w = image.shape[:2]
    dst = np.zeros((h, w), image.dtype)
    ys = np.arange(0, image.shape[0], 0.1)
    xs = np.arange(0, image.shape[1], 1)

    y1, y10 = pt1[1], pt1[1]*10
    ratios = ys / y1
    ratios[y10:] = (h - ys[y10:]) / (h - y1)

    dys = ys + ratios * (pt2[1] - pt1[1])
    ys, dys = ys.astype(int), dys.astype(int)

    ym, xm = np.meshgrid(ys, xs)
    dym, a = np.meshgrid(dys, xs)
    dst[dym, xm] = image[ym, xm]
    cv2.imshow("image", dst)

def onMouse(event, x, y, flags, param):
    global pt1, pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x, y)
        morphing1()
    elif event == cv2.EVENT_RBUTTONDOWN:
        pt1 = (x, y)
    elif event == cv2.EVENT_RBUTTONUP:
        pt2 = (x, y)
        morphing2()
    elif event == cv2.EVENT_MBUTTONDOWN:
        pt1 = pt2 = (-1, -1)
        cv2.imshow("image", image)

image = cv2.imread("images/14.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

pt1 = pt2 = (-1, -1)
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)
