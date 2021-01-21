import numpy as np, cv2
from Common.filters import filter

# 1)
image1 = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE)
gaussian = cv2.GaussianBlur(image1, (5, 5), 0.3)

# 2)
data = [ 0, -1, 0,
        -1, 5, -1,
         0, -1, 0]
mask = np.array(data, np.float32).reshape(3, 3)
sharpen = filter(image1, mask)

# 3)
image2 = cv2.imread("images/image.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(image2)

b_gaussian = cv2.GaussianBlur(b, (5, 5), 0.3)
g_gaussian = cv2.GaussianBlur(g, (5, 5), 0.3)
r_gaussian = cv2.GaussianBlur(r, (5, 5), 0.3)

b_sharpen = filter(b, mask)
g_sharpen = filter(g, mask)
r_sharpen = filter(r, mask)

rgb = cv2.merge([b, g, r])

# 4)
filter_2d = cv2.filter2D(image2, -1, mask)

cv2.imshow("gauss", gaussian)
cv2.imshow("sharpen", sharpen)
cv2.imshow("merge", rgb)
cv2.waitKey(0)
