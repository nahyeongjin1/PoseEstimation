import numpy as np, cv2

image = cv2.imread("images/image1.jpg", cv2.IMREAD_COLOR)

blue, green, red = cv2.split(image)

y = 0.299*red + 0.587*green + 0.114*blue
cb = (red-y)*0.564 + 128
cr = (blue-y)*0.713 + 128

r = y + 1.403*(cr-128)
g = y - 0.714*(cr-128) - 0.344*(cb-128)
b = y + 1.773*(cb-128)
ycbcr = cv2.merge([cr, cb, y])
rgb = cv2.merge([b, g, r])
ycbcr = cv2.convertScaleAbs(ycbcr)
rgb = cv2.convertScaleAbs(rgb)
cv2.imshow("image", image)
cv2.imshow("YCbCr", ycbcr)
cv2.imshow("RGB", rgb)
cv2.waitKey(0)
