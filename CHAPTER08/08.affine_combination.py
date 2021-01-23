import numpy as np, math, cv2
from Common.interpolation import affine_transform

def getAffineMat(center, degree, fx=1, fy=1, translate=(0,0)):
    scale_mat = np.eye(3, dtype=np.float32)
    cen_trans = np.eye(3, dtype=np.float32)
    org_trans = np.eye(3, dtype=np.float32)
    trans_mat = np.eye(3, dtype=np.float32)
    rot_mat = np.eye(3, dtype=np.float32)

    radian = degree / 180 * np.pi
    rot_mat[0] = [ np.cos(radian), np.sin(radian), 0]
    rot_mat[1] = [-np.sin(radian), np.cos(radian), 0]

    cen_trans[:2, 2] = center
    org_trans[:2, 2] = -center[0], -center[1]
    trans_mat[:2, 2] = translate
    scale_mat[0, 0], scale_mat[1, 1] = fx, fy

    ret_mat = cen_trans.dot(rot_mat.dot(trans_mat.dot(scale_mat.dot(org_trans))))
    # ret_mat = cen_trans.dot(rot_mat.dot(scale_mat.dot(trans_mat.dot(org_trans))))
    return np.delete(ret_mat, 2, axis=0)

image = cv2.imread("images/affine.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

size = image.shape[::-1]
center = np.divmod(size, 2)[0]
angle, tr = 45, (200, 0)

aff_mat1 = getAffineMat(center, angle)
aff_mat2 = getAffineMat((0, 0), 0, 2.0, 1.5)
aff_mat3 = getAffineMat(center, angle, 0.7, 0.7)
aff_mat4 = getAffineMat(center, angle, 0.7, 0.7, tr)

dst1 = cv2.warpAffine(image, aff_mat1, size)
dst2 = cv2.warpAffine(image, aff_mat2, size)
dst3 = affine_transform(image, aff_mat3)
dst4 = affine_transform(image, aff_mat4)

cv2.imshow("image", image)
cv2.imshow("dst1_only_rotate", dst1)
cv2.imshow("dst2_only_scaling", dst2)
cv2.imshow("dst3_rotate_scaling", dst3)
cv2.imshow("dst4_rotate_scaling_translate", dst4)
cv2.waitKey(0)
