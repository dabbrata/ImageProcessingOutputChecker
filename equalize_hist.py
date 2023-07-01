# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:52:50 2023

@author: WIN
"""
import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np


def makeCDF(img):
    img_h,img_w = img.shape
    histogram=np.zeros(256)
    for i in range(img_h):
        for j in range(img_w):
            histogram[img[i][j]] +=1
            
    pdf = histogram/(img_h*img_w)
    cdf = pdf
    s=pdf
    L=256
    sum=0.0
    for i in range(L):
        sum+=pdf[i]
        cdf[i]=sum
        s[i]=np.round((L-1)*cdf[i])
    return cdf

def EqualizeHistogram(img):
    img_h,img_w = img.shape
    equalized_img = np.zeros_like(img)
    histogram = np.zeros(256)
    for i in range(img_h):
        for j in range(img_w):
            histogram[img[i][j]] +=1
    pdf = histogram/(img_h*img_w)
    cdf = pdf
    s=pdf
    L=256
    sum=0.0
    for i in range(L):
        sum+=pdf[i]
        cdf[i]=sum
        s[i]=np.round((L-1)*cdf[i])
    
    for i in range(img_h):
        for j in range(img_w):
            equalized_img[i][j] = s[img[i][j]]
    
    return equalized_img

path = sys.argv[1]
img = cv2.imread(path)
plt.figure()
plt.imshow(img[:,:,::-1])
plt.title("Input")


b,g,r = cv2.split(img)

cdfnb = makeCDF(b)
plt.figure()
plt.plot(cdfnb)
plt.title('cdf non eql blue')

cdfng = makeCDF(g)
plt.figure()
plt.plot(cdfng)
plt.title('cdf non eql green')

cdfnr = makeCDF(r)
plt.figure()
plt.plot(cdfnr)
plt.title('cdf non eql red')

b = EqualizeHistogram(b)
g = EqualizeHistogram(g)
r = EqualizeHistogram(r)

plt.figure()
plt.hist(b.ravel(),256,[0,256])
plt.title("equalized b")
plt.figure()
plt.hist(g.ravel(),256,[0,256])
plt.title("equalized g")
plt.figure()
plt.hist(r.ravel(),256,[0,256])
plt.title("equalized r")

res = cv2.merge((b,g,r))

plt.figure()
plt.hist(res.ravel(),256,[0,256])
plt.title("equalized merged")

cdfb = makeCDF(b)
plt.figure()
plt.plot(cdfb)
plt.title('cdf b')

cdfg = makeCDF(g)
plt.figure()
plt.plot(cdfg)
plt.title('cdf g')

cdfr = makeCDF(r)
plt.figure()
plt.plot(cdfr)
plt.title('cdf r')




plt.figure()
plt.imshow(res[:,:,::-1],'gray')
plt.title("Output")
plt.show()



#equalization of hsv image

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img)
e_v = EqualizeHistogram(v)
e_hsv = cv2.merge((h,s,e_v))
res_hsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,15))
ax1.imshow(img[:,:,::-1])
ax1.set_title('Input image')
ax2.imshow(res_hsv[:,:,::-1])
ax2.set_title('Equalized HSV')