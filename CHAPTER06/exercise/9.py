import numpy as np, cv2

def onChangeImage1(value):
    global image1, image2, value1, value2, title, dst
    value1 = value
    image = cv2.addWeighted(image1, value1/100, image2, value2/100, 0)
    dst[:, image1.shape[1]:image3.shape[1]*2] = image
    cv2.imshow(title, dst)

def onChangeImage2(value):
    global image1, image2, value1, value2, title, dst
    value2 = value
    image = cv2.addWeighted(image1, value1/100, image2, value2/100, 0)
    dst[:, image1.shape[1]:image3.shape[1] * 2] = image
    cv2.imshow(title, dst)

image1 = cv2.imread("images/image1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/image2.jpg", cv2.IMREAD_GRAYSCALE)
image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

dst = np.zeros((image1.shape[0], image1.shape[1]*3), np.uint8)
dst[:, :image1.shape[1]] = image1
dst[:, image1.shape[1]:image3.shape[1]*2] = image3
dst[:, image3.shape[1]*2:image2.shape[1]*3] = image2

title = "dst"
value1, value2 = 50, 50
cv2.namedWindow(title)
cv2.imshow(title, dst)
cv2.createTrackbar("image1", title, 50, 100, onChangeImage1)
cv2.createTrackbar("image2", title, 50, 100, onChangeImage2)


cv2.waitKey(0)
cv2.destroyAllWindows()
