import sys

import numpy as np
import matplotlib.pyplot as plt
import cv2
import math


def bilinear_interpolation(img, x, y):
    height, width, channels = img.shape
    x_floor = int(np.floor(x))
    y_floor = int(np.floor(y))
    x_ceil = min(x_floor + 1, width - 1)
    y_ceil = min(y_floor + 1, height - 1)
    dx = x - x_floor
    dy = y - y_floor

    top_left = img[y_floor, x_floor] * (1 - dx) * (1 - dy)
    top_right = img[y_floor, x_ceil] * dx * (1 - dy)
    bottom_left = img[y_ceil, x_floor] * (1 - dx) * dy
    bottom_right = img[y_ceil, x_ceil] * dx * dy

    interpolated_pixel = top_left + top_right + bottom_left + bottom_right

    return interpolated_pixel.astype(np.uint8)
def Ripple(img,tx,ty,ax,ay):
    out = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    img_h,img_w = img.shape[:2]
    out_h,out_w = out.shape[:2]
    for i in range(img_h):
        for j in range(img_w):
            x = int(j+(ax*math.sin((2*np.pi*i)/tx)))
            y = int(i+(ay*math.sin((2*np.pi*j)/ty)))
            if 0<=x<img_w and 0<=y<img_h:
                out[i][j] = bilinear_interpolation(img, x, y)
    return out

path = sys.argv[1]
img = cv2.imread(path)
out = Ripple(img,tx=30,ty=20,ax=10,ay=10)

plt.figure()
plt.imshow(img[:,:,::-1],'gray')
plt.title('Input')
plt.figure()
plt.imshow(out[:,:,::-1])
plt.title('Output')

plt.show()