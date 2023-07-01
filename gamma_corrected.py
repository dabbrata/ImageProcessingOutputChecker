import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import sys


#res = c*s^gamma
def Gamma(img):
    gm=.5
    c=255/255**gm
    res = np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i][j] = c*(img[i][j]**gm)
    res = (res-np.min(res))/(np.max(res)-np.min(res))
    return res

path = sys.argv[1]
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

b,g,r = cv2.split(img)
c1 = Gamma(b)
c2 = Gamma(g)
c3 = Gamma(r)
resC = cv2.merge((c1,c2,c3))
plt.figure()
plt.imshow(img[:,:,::-1])
plt.title('Input image')
plt.figure()
plt.imshow(resC[:,:,::-1])
plt.title('Gamma Corrected Image')

plt.show()