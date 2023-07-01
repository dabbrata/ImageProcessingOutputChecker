import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def HomoFilter(img):
    img_h,img_w = img.shape
    homo_filter = np.zeros((img_h,img_w),dtype=np.float32)
    gh=1.2
    gl=.5
    c=.1
    d0 = 50
    center_i,center_j = img_h//2,img_w//2
    for i in range(img_h):
        for j in range(img_w):
            duv = (i-center_i)**2 + (j-center_j)**2
            homo_filter[i][j] = (gh-gl)*(1-np.exp(-c*(duv/d0**2)))+gl
    return homo_filter


def ApplyFilter(img,homo_filter):
    loged = np.log1p(img)
    F = np.fft.fft2(loged)
    F_shift = np.fft.fftshift(F)
    G = F_shift*homo_filter
    IFS = np.fft.ifftshift(G)
    IF = np.fft.ifft2(IFS)
    ans = np.exp(np.real(IF))
    return ans.astype(np.uint8)

path = sys.argv[1]
img = cv2.imread(path,0)
plt.figure()
plt.imshow(img,'gray')
plt.title("Input image")

hom_filt = HomoFilter(img)
res = ApplyFilter(img, hom_filt)

plt.figure()
plt.imshow(res,'gray')
plt.title("Homomorphic filtered image")
plt.show()


