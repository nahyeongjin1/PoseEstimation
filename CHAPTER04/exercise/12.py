import numpy as np
import cv2


def onChange(value):
    global image, title, pos

    add_value = value - int(image[0][0])
    pos += add_value
    print("추가 화소값:", add_value)
    image = image + add_value
    cv2.imshow(title, image)


pos = 0
image = np.zeros((300, 500), np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, pos, 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    if key == 2424832 and pos >= 1:  # 왼쪽 키
        pos -= 1
        cv2.setTrackbarPos("Brightness", title, pos)
        image -= 1
        cv2.imshow(title, image)
    elif key == 2555904 and pos <= 254:  # 오른쪽 키
        pos += 1
        cv2.setTrackbarPos("Brightness", title, pos)
        image += 1
        cv2.imshow(title, image)

cv2.destroyAllWindows()

"""
한 쪽 방향으로 계속 증가시킨다고 했을 때, 처음만 1 증가하고 그 이후로는 계속 2씩 증가함
왼쪽 오른쪽 둘 다 그럼
그리고 내렸을 때 회색으로 고정되는거, 아무리 봐도 이유를 모르겠음
"""