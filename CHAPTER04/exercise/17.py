import numpy as np
import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("카메라 연결 안됨")

fps = 15
delay = round(1000/fps)
size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 카메라 속성 실행창에 출력
print("width x height: ", size)
print("VideoWriterfourcc: %s" % fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)

capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

# 동영상파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("images/flip_test.avi", fourcc, fps, size)
if not writer.isOpened(): raise Exception("동영상파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    frame = frame[:, ::-1]
    writer.write(frame)
    cv2.imshow("View Frame from Camera", frame)

writer.release()
capture.release()

# 문제 없음
