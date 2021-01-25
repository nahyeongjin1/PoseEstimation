import numpy as np, cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

def onMouse(event, x, y, flags, param):
    global pts1, pts2, image
    if event == cv2.EVENT_LBUTTONDOWN:
        pts1 = (x, y)
    if event == cv2.EVENT_LBUTTONUP:
        pts2 = (x, y)
        pt = (pts2[0]-pts1[0], pts2[1]-pts1[1])
        image = translate(image, pt)
        cv2.imshow("image", image)


image = cv2.imread("images/13.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse)
cv2.waitKey(0)
