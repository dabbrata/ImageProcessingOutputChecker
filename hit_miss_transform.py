import sys

import matplotlib.pyplot as plt
import cv2
import numpy as np

def HitorMiss(img,kernel):
    kernel = ((kernel*255).astype(np.uint8))
    w = np.ones((150,150),dtype=np.uint8)*255
    x=cv2.resize(kernel,None,fx=50,fy=50,interpolation=cv2.INTER_NEAREST)
    B1 = x
    B2 = w-x
    plt.figure()
    plt.imshow(B1,'gray')
    Ac = 255-img
    erode1 = cv2.erode(img,B1,iterations=1)
    erode2 = cv2.erode(Ac,B2,iterations=1)
       
    return erode1 & erode2    

path = sys.argv[1]
img = cv2.imread(path,0)


plt.figure()
plt.imshow(img,'gray')
plt.title("input")

x1 = np.array(([0,0,0],
               [1,1,0],
               [1,0,0]))

x2 = np.array(([0,1,1],
               [0,0,1],
               [0,0,1]))

x3 = np.array(([1,1,1],
               [0,1,0],
               [0,1,0]))



res1 = HitorMiss(img, x1)
plt.figure()
plt.imshow(res1,'gray')
plt.title("SE: ([0,0,0],[1,1,0],[1,0,0])")

res2 = HitorMiss(img, x2)
plt.figure()
plt.imshow(res2,'gray')
plt.title("SE: ([0,1,1],[0,0,1],[0,0,1])")

res3 = HitorMiss(img, x3)
plt.figure()
plt.imshow(res3,'gray')
plt.title("SE: ([1,1,1],[0,1,0],[0,1,0])")

plt.show()


