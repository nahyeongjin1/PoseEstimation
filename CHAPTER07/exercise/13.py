import numpy as np, cv2
from Common.filters import filter, filter2

image = cv2.imread("images/13.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]
mask = np.array(data, np.float32).reshape(3, 3)

blur1 = filter(image, mask)
blur2 = filter2(image, mask)
blur3 = cv2.blur(image, (3, 3))

blur1 = blur1.astype('uint8')
blur2 = cv2.convertScaleAbs(blur2)

cv2.imshow("blur1", blur1)
cv2.imshow("blur2", blur2)
cv2.imshow("blur3", blur3)
cv2.waitKey(0)