import numpy as np, cv2

def myFilter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += image[y, x] * mask[u, v]
            dst[i, j] = sum
    return dst

def differential(image, data1, data2, mask_name):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = myFilter(image, mask1)
    dst2 = myFilter(image, mask2)

    if mask_name == "roberts":
        dst1, dst2 = np.abs(dst1), np.abs(dst2)
        dst = cv2.magnitude(dst1, dst2)

        dst = np.clip(dst, 0, 255).astype('uint8')
        return dst
    elif mask_name == "prewitt":
        dst = cv2.magnitude(dst1, dst2)
        dst = cv2.convertScaleAbs(dst)
        return dst
    elif mask_name == "sobel":
        dst1 = cv2.convertScaleAbs(dst1)
        dst2 = cv2.convertScaleAbs(dst2)

        return dst1, dst2

image = cv2.imread("images/11.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

roberts_mask1 = [[-1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0]]
roberts_mask2 = [[0, 0, -1],
                 [0, 1, 0],
                 [0, 0, 0]]
prewitt_mask1 = [[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]]
prewitt_mask2 = [[-1, -1, -1],
                 [0, 0, 0],
                 [1, 1, 1]]
sobel_mask1 = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]
sobel_mask2 = [[-1, -2, -1],
               [0, 0, 0],
               [-1, -2, -1]]

roberts_dst = differential(image, roberts_mask1, roberts_mask2, "roberts")
prewitt_dst = differential(image, prewitt_mask1, prewitt_mask2, "prewitt")
sobel_dst1, sobel_dst2 = differential(image, sobel_mask1, sobel_mask2, "sobel")

cv2.imshow("image", image)
cv2.imshow("roberts", roberts_dst)
cv2.imshow("prewitt", prewitt_dst)
cv2.imshow("sobel- vertical", sobel_dst1)
cv2.imshow("sobel- horizontal", sobel_dst2)
cv2.waitKey(0)
