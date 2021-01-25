import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global pts1, pts2
    if event == cv2.EVENT_LBUTTONDOWN:
        pts1 = (x, y)
    if event == cv2.EVENT_LBUTTONUP:
        pts2 = (x, y)
        cv2.line(image, pts1, pts2, (255, 0, 0))
        cv2.imshow("image", image)
        gradient = -(pts1[1] - pts2[1]) / (pts1[0] - pts2[0])
        length = np.sqrt((pts1[0] - pts2[0])**2 + (pts1[1] - pts2[1])**2)
        print("기울기: %.2f" % gradient)
        print("길이: %.2f" % length)


image = cv2.imread("images/13.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse)
cv2.waitKey(0)
