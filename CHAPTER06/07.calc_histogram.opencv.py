import numpy as np, cv2

def calc_histo(image, histSize, ranges=[0, 256]):
    hist = np.zeros((histSize, 1), np.float32)
    gap = ranges[1] / histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1

    return hist
