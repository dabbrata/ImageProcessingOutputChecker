import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import sys

def ContrastStretching(img):
    res = np.zeros((img.shape[0],img.shape[1]))
    mx = np.max(img)
    mn = np.min(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i][j] = (img[i][j] - mn)/(mx-mn)
            
    return res

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
img = cv2.imread(r"C:\Users\WIN\Desktop\image_lab\Lena.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

b,g,r = cv2.split(img)
i1 = InverseLog(b)
i2 = InverseLog(g)
i3 = InverseLog(r)
resI = cv2.merge((i1,i2,i3))
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,15))
ax1.imshow(img[:,:,::-1])
ax1.set_title('Input image')
ax2.imshow(resI[:,:,::-1])
ax2.set_title('Inversed Log Image')


b,g,r = cv2.split(img)
g1 = Gamma(b)
g2 = Gamma(g)
g3 = Gamma(r)
resG = cv2.merge((g1,g2,g3))
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,15))
ax1.imshow(img[:,:,::-1])
ax1.set_title('Input image')
ax2.imshow(resG[:,:,::-1])
ax2.set_title('Gamma Corrected Image')



b,g,r = cv2.split(img)
c1 = ContrastStretching(b)
c2 = ContrastStretching(g)
c3 = ContrastStretching(r)
resC = cv2.merge((b,g,r))
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,15))
ax1.imshow(img[:,:,::-1])
ax1.set_title('Input image')
ax2.imshow(resC[:,:,::-1])
ax2.set_title('Contrast Stretched Image')