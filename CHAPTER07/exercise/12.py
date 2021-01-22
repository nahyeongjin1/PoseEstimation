import numpy as np, cv2

image = cv2.imread("images/12.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

# 라플라시안
laplacian_data = [[-1, -1, -1],
                  [-1, 8, -1],
                  [-1, -1, -1]]
laplacian_mask = np.array(laplacian_data, np.int16)

laplacian_dst = cv2.filter2D(image, cv2.CV_16S, laplacian_mask)
laplacian_dst = cv2.convertScaleAbs(laplacian_dst)

# LoG
gaus = cv2.GaussianBlur(image, (7, 7), 0)
LoG_dst = cv2.Laplacian(gaus, cv2.CV_16S, ksize=9)

# DoG
gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
DoG_dst = gaus1 - gaus2

cv2.imshow("Laplacian", laplacian_dst)
cv2.imshow("LoG", LoG_dst)
cv2.imshow("DoG", DoG_dst)
cv2.waitKey(0)
