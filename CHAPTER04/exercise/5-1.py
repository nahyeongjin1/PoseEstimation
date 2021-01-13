import numpy as np, cv2

image = np.zeros((300, 400), np.uint8)
image[:] = 100

title = 'Window'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.moveWindow(title, 100, 200)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
(x,y) = (100,200) 에서부터 row가 300, column이 400인 grayscale image를 띄운다
WINDOW_NORMAL이기 때문에 윈도우 창 크기 조절 가능
"""