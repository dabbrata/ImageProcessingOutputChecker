import sys

import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

def twirl_image(image, center, angle, rmax):
    image = image.astype(np.float32) / 255.0
    height, width = image.shape[:2]
    y, x = np.mgrid[0:height, 0:width]
    x -= center[0]
    y -= center[1]
    distance = np.sqrt(x**2 + y**2)
    beta = np.arctan2(y,x) + angle * ((rmax-distance) / rmax)
    
    x_new = distance * np.cos(beta)
    y_new = distance * np.sin(beta)

    x_new += center[0]
    y_new += center[1]

    mask = distance > rmax

    x_new[mask] = x[mask] + center[0]
    y_new[mask] = y[mask] + center[1]

    twirled_image = cv2.remap(image, x_new.astype(np.float32), y_new.astype(np.float32),
                              interpolation=cv2.INTER_LINEAR)

    return (twirled_image * 255).astype(np.uint8)

path = sys.argv[1]
image = cv2.imread(path)

img_w,img_h = image.shape[:2]
center = (img_w // 2, img_h // 2)
rotation_angle = 90  
max_radius = min(center[0], center[1]) 

twirled_image = twirl_image(image, center, np.radians(rotation_angle), max_radius)


plt.figure()
plt.imshow(image[:,:,::-1])
plt.title("Original Image")
plt.axis("off")

plt.figure()
plt.imshow(twirled_image[:,:,::-1])
plt.title("Twirled Image")
plt.axis("off")
plt.show()



