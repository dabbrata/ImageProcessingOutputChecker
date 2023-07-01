import cv2
import matplotlib.pyplot as plt
import numpy as np

def getPoints(img,num):
    fig,ax = plt.subplots(1,figsize=(10,15))
    plt.imshow(img,cmap='gray')
    pts = np.uint16(np.round(np.array(plt.ginput(n=num))))
    plt.close()
    return pts

img = cv2.imread(r"C:\Users\WIN\Downloads\noiseball.png",0)
plt.figure()
plt.imshow(img,'gray')

F = np.fft.fft2(img)
F_shift = np.fft.fftshift(F)

magnitude = np.log(np.abs(F))
magnitude_shift = np.log(np.abs(F_shift))

plt.figure()
plt.imshow(magnitude_shift,'gray')
plt.title("Magnitude shift")

pts = getPoints(magnitude_shift,6)

butter_filter = np.zeros((img.shape[0],img.shape[1]),dtype = np.float32)

print(pts)
n = input("n :")
d0 = input("Radius : ")
n = np.uint8(n)
d0 = np.uint8(d0)

u=[]
v=[]

for i in range(len(pts)):
    x,y = pts[i]
    v.append(x)
    u.append(y)

print(v,u)

center_i = img.shape[0]//2
center_j = img.shape[1]//2
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        prod=1
        for k in range(len(v)):
            duv = np.sqrt((i-center_i-(u[k]-center_i))**2+(j-center_j-(v[k]-center_j))**2)
            dmuv = np.sqrt((i-center_i+(u[k]-center_i))**2+(j-center_j+(v[k]-center_j))**2)
            prod *= (1/(1+(d0/duv)**(2*n))) * (1/(1+(d0/dmuv)**(2*n)))
        butter_filter[i,j] = prod
        
        
plt.figure()
plt.imshow(butter_filter,'gray')
plt.title("notch filter")

G_S = F_shift*butter_filter
G = np.fft.ifftshift(G_S)
output = np.fft.ifft2(G).real

plt.figure()
plt.imshow(output,'gray')
plt.show()