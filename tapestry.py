import sys

import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
from scipy.interpolate import interp2d


def Tapestry(img,tx,ty,a):
    img_h,img_w = img.shape[:2]
    out = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    out_h,out_w = out.shape[:2]
    xc = out_w//2
    yc = out_h//2
    print(out.shape)
    
    
    x,y = np.meshgrid(np.arange(1,img_w+1),np.arange(1,img_h+1))
    u = x + a * np.sin((2 * np.pi / tx) * (x - xc))
    v = y + a * np.sin((2 * np.pi / ty) * (y - yc))
    
    res = cv2.remap(img,u.astype(np.float32),v.astype(np.float32),interpolation=cv2.INTER_LINEAR)
    
    return res

path = sys.argv[1]
img = cv2.imread(path)
img = img[:,:,::-1]
plt.figure()
plt.imshow(img)
plt.title("Input")

res = Tapestry(img, tx=30, ty=30, a=5)
plt.figure()
plt.imshow(res,'gray')
plt.title("Output")
plt.show()