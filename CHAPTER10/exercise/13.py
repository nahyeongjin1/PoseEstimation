# 10.3절에서 검출된 숫자 객체를 중앙에 배치하는 place_middle()함수를 직접 구현하시오.
# 단, 교재 소스와는 다르게 자신의 방식으로 구현하시오.

import numpy as np, cv2

def place_middle(number, new_size):
    h, w = number.shape[:2]
    big = max(h, w)
    square = np.full((big, big), 255, np.float32)

    dx, dy = np.subtract(big, (w, h)) // 2
    square[dy:dy+h, dx:dx+w] = number
    return cv2.resize(square, new_size).flatten()