import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np


def median_filter(image, kernel_size):
    height, width = image.shape
    img_padded = np.pad(image, (kernel_size // 2, kernel_size // 2), mode='constant')
    img_filtered = np.zeros(image.shape)

    for i in range(height):
        for j in range(width):
            kernel_portion = img_padded[i:i + kernel_size, j:j + kernel_size]
            kernel_flattened = kernel_portion.flatten()

            sorted_vals = sorted(kernel_flattened)
            mid_index = len(sorted_vals) // 2
            median_value = sorted_vals[mid_index]

            img_filtered[i, j] = median_value

    return img_filtered

path = sys.argv[1]
grayImg = cv2.imread(path,0)
i = median_filter(grayImg,5)
plt.figure()
plt.imshow(grayImg,'gray')
plt.title("Input")

plt.figure()
plt.imshow(i,'gray')
plt.title("Mdian filtered image")
plt.show()