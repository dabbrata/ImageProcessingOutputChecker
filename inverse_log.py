import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import sys

# s=c*log(1+r)
# r = 2^(s/c) - 1
def InverseLog(img):
    c = 255/math.log2(1+255)
    res = np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i][j] = pow(2,(img[i][j]/c))-1
    res = (res-np.min(res))/(np.max(res)-np.min(res))
    return res

path = sys.argv[1]
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

b,g,r = cv2.split(img)
c1 = InverseLog(b)
c2 = InverseLog(g)
c3 = InverseLog(r)
resC = cv2.merge((c1,c2,c3))
plt.figure()
plt.imshow(img[:,:,::-1])
plt.title('Input image')
plt.figure()
plt.imshow(resC[:,:,::-1])
plt.title('Inverse logged Image')

plt.show()