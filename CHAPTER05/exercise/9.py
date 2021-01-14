import numpy as np, cv2

array = (np.random.rand(3, 6) * 10)
col_avg = cv2.reduce(array, 0, cv2.REDUCE_AVG)
row_avg = cv2.reduce(array, 1, cv2.REDUCE_AVG)

print(array)
print()
print(col_avg)
print()
print(row_avg)
