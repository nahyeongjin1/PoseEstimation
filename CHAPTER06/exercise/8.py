import numpy as np, cv2

image1 = cv2.imread("images/image1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/image2.jpg", cv2.IMREAD_GRAYSCALE)

image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

dst = np.zeros((image1.shape[0], image1.shape[1]*3), np.uint8)
dst[:, :image1.shape[1]] = image1
dst[:, image1.shape[1]:image3.shape[1]*2] = image3
dst[:, image3.shape[1]*2:image2.shape[1]*3] = image2

cv2.imshow("dst", dst)
cv2.waitKey(0)
