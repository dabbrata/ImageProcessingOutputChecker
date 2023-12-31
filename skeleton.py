import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

path = sys.argv[1]
img = cv2.imread(path, 0)
img_h, img_w = img.shape



# Thresholding
img = (img > 170).astype(np.uint8)

plt.figure()
plt.imshow(img, 'gray')
plt.title('Input')

A = 1 - img

kernel = np.ones((3, 3), dtype=np.uint8)
skeleton = np.zeros((img_h, img_w), dtype=np.uint8)

k = 1
while True:
    er = cv2.erode(A, kernel, iterations=k)

    if np.sum(er) == 0:
        break

    op = cv2.morphologyEx(er, cv2.MORPH_OPEN, kernel)
    skeleton = skeleton | (er - op)

    k += 1

plt.figure()
plt.imshow(skeleton, 'gray')
plt.title('Output(skeletoned)')
plt.show()