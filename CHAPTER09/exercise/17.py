import numpy as np, cv2
from Common.dct2d import dct2, idct2, scipy_dct2, scipy_idct2

def dct2_mode(block, mode):
    if mode==1: return dct2(block)
    elif mode==2: return scipy_dct2(block)
    elif mode==3: return cv2.dct(block.astype('float32'))

def idct2_mode(block, mode):
    if mode==1: return idct2(block)
    elif mode==2: return scipy_idct2(block)
    elif mode==3: return cv2.dct(block, flags=cv2.DCT_INVERSE)

def dct_filtering(img, filter, M, N):
    dst = np.empty(img.shape, np.float32)
    for i in range(0, img.shape[0], M):
        for j in range(0, img.shape[1], N):
            block = img[i:i+M, j:j+N]
            new_block = dct2_mode(block, mode)
            if new_block.shape!=(8,8): continue
            new_block = new_block * filter
            dst[i:i+M, j:j+N] = idct2_mode(new_block, mode)
    return cv2.convertScaleAbs(dst)

image = cv2.imread("images/dct.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

mode = 3
M, N = 8, 8
filters = [np.zeros((M,N), np.float32) for i in range(5)]
titles = ['DC Pass', 'High Pass', 'Low Pass', 'Vertical Pass', 'Horizontal Pass']

filters[0][0, 0] = 1
filters[1][:], filters[1][0, 0] = 1, 0
filters[2][:M//2, :N//2] = 1
filters[3][1:, 0] = 1
filters[4][0, 1:] = 1

for filter, title in zip(filters, titles):
    dst = dct_filtering(image, filter, M, N)
    cv2.imshow(title, dst)
cv2.imshow("image", image)
cv2.waitKey(0)