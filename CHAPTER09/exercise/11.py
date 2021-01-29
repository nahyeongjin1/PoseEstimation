import numpy as np, cv2
from Common.dft2d import exp, calc_spectrum, fftshift
from Common.fft2d import zeropadding

def butterfly(pair, L, N, dir):
    for k in range(L):
        Geven, Godd = pair[k], pair[k+L]
        pair[k]   = Geven + Godd * exp(dir * k / N)
        pair[k+L] = Geven - Godd * exp(dir * k / N)

def pairing(g, N, dir, start=0, stride=1):
    if N == 1: return [g[start]]
    L = N // 2
    sd = stride * 2
    part1 = pairing(g, L, dir, start, sd)
    part2 = pairing(g, L, dir, start+stride, sd)
    pair = part1 + part2
    butterfly(pair, L, N, dir)
    return pair

def fft(g):
    return pairing(g, len(g), 1)

def fft2(image):
    pad_img = zeropadding(image)
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)


image = cv2.imread("images/11.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dft1 = fft2(image)

spectrum = calc_spectrum(fftshift(dft1))


cv2.imshow("spectrum", spectrum)

cv2.waitKey(0)