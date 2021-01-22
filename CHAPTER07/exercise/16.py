import numpy as np, cv2

def erode(img, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    mcnt = cv2.countNonZero(mask)
    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = img[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)
            dst[i, j] = 255 if (cnt == mcnt) else 0
    return dst

def dilate(img, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = img[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)
            dst[i, j] = 0 if (cnt == 0) else 255
    return dst

def morphology(th_img, morph, mask=None):
    if morph == "erode":
        if mask is None:
            dst = erode(th_img)
        else:
            dst = erode(th_img, mask)
    elif morph == "dilate":
        if mask is None:
            dst = dilate(th_img)
        else:
            dst = dilate(th_img, mask)
    else:
        dst = None
    return dst

image = cv2.imread("images/16.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],
                 [1, 1, 1],
                 [0, 1, 0]]).astype('uint8')
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]

erode_img = morphology(th_img, "erode", mask)
dilate_img = morphology(th_img, "dilate", mask)

cv2.imshow("erode", erode_img)
cv2.imshow("dilate", dilate_img)
cv2.waitKey(0)
