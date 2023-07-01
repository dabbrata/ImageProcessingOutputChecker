# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 00:00:20 2023

@author: WIN
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2

def FlipKernel(kernel):
    k_h,k_w = kernel.shape
    k = np.zeros_like(kernel)
    for i in range(k_h):
        for j in range(k_w):
            k[i][j] = kernel[k_h-i-1][k_w-j-1]
    return k

def Convolution(img,kernel):
    # kernel = FlipKernel(kernel)
    # k_h,k_w = kernel.shape
    # res = np.zeros_like(img)
    # padded_img = np.pad(img,(k_h//2,k_w//2),mode='constant')
    # p_h,p_w = padded_img.shape
    # i_h,i_w = img.shape
    # for i in range(i_h):
    #     for j in range(i_w):
    #         neighbour = padded_img[i:i+k_h,j:j+k_w]
    #         result = neighbour*kernel
    #         summ = np.sum(result)
    #         res[i][j] = summ
    # return res

    return cv2.filter2D(img,-1,kernel)

            

path = sys.argv[1]
img = cv2.imread(path,0)
plt.figure()
plt.imshow(img,'gray')
plt.title("Input image")

k2=np.ones((9,9))/81
output = Convolution(img, k2)
plt.figure()
plt.imshow(output,'gray')
plt.title("Mean filtered image")
plt.show()
