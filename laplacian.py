import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

path = sys.argv[1]
grayImg = cv2.imread(path,0)

k1 = np.array([[0,1,0],
             [1,-4,1],
             [0,1,0]])
k2 = np.array([[0,-1,0],
             [-1,4,-1],
             [0,-1,0]])
k3 = np.array([[1,1,1],
             [1,-8,1],
             [1,1,1]])
k4 = np.array([[-1,-1,-1],
             [-1,8,-1],
             [-1,-1,-1]])
i1 = cv2.filter2D(grayImg,-1,k1)
i2 = cv2.filter2D(grayImg,-1,k2)
i3 = cv2.filter2D(grayImg,-1,k3)
i4 = cv2.filter2D(grayImg,-1,k4)

th = 50
i1 = i1 > th
i2 = i2 > th
i3 = i3 > th
i4 = i4 > th

#i5 = cv2.filter2D(grayImg,-1,k1)
plt.figure()
plt.imshow(grayImg,'gray')
plt.title("Input image")
plt.figure()
plt.imshow(i1,'gray')
plt.title("for kernal [[0,1,0],[1,-4,1],[0,1,0]]")
plt.figure()
plt.imshow(i2,'gray')
plt.title("for kernel [[0,-1,0],[-1,4,-1],[0,-1,0]]")
plt.figure()
plt.imshow(i3,'gray')
plt.title("for kernel [[1,1,1],[1,-8,1],[1,1,1]]")
plt.figure()
plt.imshow(i4,'gray')
plt.title("for kernel [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]")

plt.show()
