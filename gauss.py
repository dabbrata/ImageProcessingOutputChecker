import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np


def makeKernel(k_size, sigma):
    n = k_size // 2
    kernel = np.zeros((k_size, k_size))
    for i in range(k_size):
        for j in range(k_size):
            x = n - i
            y = n - j
            gp = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
            gp = (1 / (2 * np.pi * sigma ** 2)) * gp
            kernel[i][j] = gp
    return kernel


path = sys.argv[1]
img = cv2.imread(path, 0)
plt.figure()
plt.imshow(img, 'gray')
plt.title("input")

k = makeKernel(15, 2)
plt.figure()
plt.imshow(k, 'gray')
res = cv2.filter2D(img, -1, k)
plt.figure()
plt.imshow(res, 'gray')
plt.show()
