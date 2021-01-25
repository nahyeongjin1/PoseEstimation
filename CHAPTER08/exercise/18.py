import numpy as np
import cv2

def draw_bar(img, pt, w, bars):
    pt = np.array(pt, np.int)
    for bar in bars:
        (x, y), h = pt, w*6
        cv2.rectangle(img, (x, y, w, h), (0, 0, 0), -1)
        if bar == 0:
            y = 400 - 400 // 48
            h = w // 2
            cv2.rectangle(img, (x, y, w, h), (255, 255, 255), -1)
        pt += (int(w*1.5), 0)

image = np.ones((800, 1200, 3), np.uint8) * 255
radius = 200
red, blue = (0, 0, 255), (255, 0, 0)

cv2.ellipse(image, (600, 400), (radius, radius), 0, 0, -180, red, -1)
cv2.ellipse(image, (600, 400), (radius, radius), 0, 0, 180, blue, -1)
cv2.ellipse(image, (500, 400), (radius//2, radius//2), 0, 0, 180, red, -1)
cv2.ellipse(image, (700, 400), (radius//2, radius//2), 0, 0, -180, blue, -1)

draw_bar(image, (600-radius-7*400//12, 400-400//4), 400//12, (1,1,1))
draw_bar(image, (600+radius+400//4, 400-400//4), 400//12, (0,0,0))

cv2.imshow("18", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
