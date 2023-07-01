import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

point_list=[]
def getPoints(img):
    # click and seed point set up
    x = None
    y = None

    # The mouse coordinate system and the Matplotlib coordinate system are different, handle that
    def onclick(event):
        global x, y
        ax = event.inaxes
        if ax is not None:
            x, y = ax.transData.inverted().transform([event.x, event.y])
            x = int(round(x))
            y = int(round(y))
            point_list.append((x,y))


    X = np.zeros_like(img)
    plt.title("Please select seed pixel from the input")
    im = plt.imshow(img, cmap='gray')
    im.figure.canvas.mpl_connect('button_press_event', onclick)
    plt.show(block=True)
    
    return point_list

img = cv2.imread(r"C:\Users\WIN\Downloads\th_img2.jpg", 0)
img_h, img_w = img.shape

pts = getPoints(img)
print(pts)

# plt.imshow(img, 'gray')
# plt.title('Input')
# plt.show()
A = np.round(img / 255.0).astype(np.uint8)
x0 = np.zeros((img_h, img_w), dtype=np.uint8)

# x0[125, 223] = 1
# x0[388, 197] = 1
# x0[405, 343] = 1
for i in range(len(pts)):
    x,y=pts[i]
    x0[y,x]=1
print(x0)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
print(kernel)
Ac = 1-A
while True:
    x1 = cv2.dilate(x0, kernel, iterations=1) & Ac
    if np.sum(x1 != x0) == 0:
        break
        
    x0 = x1
    
output = A | x1

plt.imshow(output, cmap='gray')
plt.title('Output')
plt.show()