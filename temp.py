import cv2
import matplotlib.pyplot as plt
import numpy as np

def GetPoints(image,numPoints):
    %matplotlib
    fig,ax = plt.subplots(1,figsize=(15,10))
    plt.imshow(image,cmap='gray')
    pts = np.uint16(np.round(np.array(plt.ginput(n=numPoints))))
    #pts = pts[:,[1,0]].T
    plt.close
    return pts

img = cv2.imread(r"C:\Users\WIN\Downloads\th_img2.jpg", 0)
img_h, img_w = img.shape

plt.figure()
plt.imshow(img, 'gray')
plt.title('Input')

A = np.round(img / 255.0).astype(np.uint8)

x0 = np.zeros((img_h, img_w), dtype=np.uint8)
pts = GetPoints(img, 3)
for i in range(len(pts)):
    x,y = pts[i]
    x0[y,x] = 1

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
Ac = 1-A
while True:
    x1 = cv2.dilate(x0, kernel, iterations=1) & Ac
    
    if np.sum(x1 != x0) == 0:
        break
        
    x0 = x1
    
output = A | x1

plt.figure()
plt.imshow(output, 'gray')
plt.title('Output')
plt.show()