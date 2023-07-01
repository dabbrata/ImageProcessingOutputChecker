import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import sys


def ContrastStretching(img):
    res = np.zeros((img.shape[0], img.shape[1]))
    mx = np.max(img)
    mn = np.min(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i][j] = (img[i][j] - mn) / (mx - mn)

    return res


path = sys.argv[1]
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

b,g,r = cv2.split(img)
c1 = ContrastStretching(b)
c2 = ContrastStretching(g)
c3 = ContrastStretching(r)
resC = cv2.merge((c1,c2,c3))
plt.figure()
plt.imshow(img[:,:,::-1])
plt.title('Input image')
plt.figure()
plt.imshow(resC[:,:,::-1])
plt.title('Contrast Stretched Image')

plt.show()