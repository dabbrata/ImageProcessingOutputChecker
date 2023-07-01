import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

path = sys.argv[1]
grayImg = cv2.imread(path,0)

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_x = cv2.filter2D(grayImg,-1,sobel_x)
edge_y = cv2.filter2D(grayImg,-1,sobel_y)

Gm = np.sqrt(edge_x ** 2 + edge_y ** 2)
direction = np.arctan2(edge_y, edge_x)

th = 50
img_x = edge_x>th
img_y = edge_y>th

Gm = (((Gm - np.min(Gm))/(np.max(Gm) - np.min(Gm)))*255).astype(np.uint8)
Gm = Gm > th

print()
plt.figure()
plt.imshow(grayImg,'gray')
plt.title("Input image")
plt.figure()
plt.imshow(img_x,'gray')
plt.title("x-direction")
plt.figure()
plt.imshow(img_y,'gray')
plt.title("y-direction")
plt.figure()
plt.imshow(Gm,'gray')
plt.title("Gradient of magnitude")
plt.figure()
plt.imshow(direction,'gray')
plt.title("Direction")

plt.show()