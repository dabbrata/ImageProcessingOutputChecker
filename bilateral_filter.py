import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

path = sys.argv[1]
img = cv2.imread(path,0)
plt.figure()
plt.imshow(img,'gray')

def Gaussian(k_sz,sigma):
    res = np.zeros((k_sz,k_sz))
    center_i,center_j = k_sz//2,k_sz//2
    for i in range (k_sz):
        for j in range(k_sz):
            x = i-center_i
            y = j-center_j
            g = np.exp(-(x**2+y**2)/(2*sigma**2))/(2*np.pi*sigma**2)
            res[i][j] = g
    return res

def Epanechnikov(k_sz,sigma):
    resu = np.zeros((k_sz,k_sz),np.float64)
    for i in range(k_sz):
        for j in range(k_sz):
            d = (i-0-k_sz//2)**2 + (j-0-k_sz//2)**2
            res = d/(k_sz//2)**2 
            res = max(0,1-res)
            resu[i][j] = res
    return resu
            
spatial_kernel = Epanechnikov(7,2)
rate = 50
kernel2 = cv2.resize(spatial_kernel, None, fx = rate, fy = rate, interpolation = cv2.INTER_NEAREST)
plt.figure()
plt.imshow(kernel2,'gray')
def BilateralFilter(img,kernel,sigma):
    img_h,img_w = img.shape
    n=len(kernel)
    padded_img = np.pad(img,(n//2,n//2),mode='constant')
    padded_img = np.float64(padded_img)
    filtered = np.zeros(img.shape,dtype = np.float64)
    for i in range(img_h):
        for j in range(img_w):
            neighbour = padded_img[i:i+n,j:j+n]
            center = padded_img[i+n//2][j+n//2]
            range_kernel = np.exp(-(((center-neighbour)**2)/(2*(sigma**2))))
            bilateral_kernel = range_kernel*kernel
            conv = neighbour*bilateral_kernel
            conv = np.sum(conv)
            res = conv/np.sum(bilateral_kernel)
            filtered[i][j] = res
    return filtered

out = BilateralFilter(img, spatial_kernel,80)
plt.figure()
plt.imshow(out,'gray')
plt.show()
