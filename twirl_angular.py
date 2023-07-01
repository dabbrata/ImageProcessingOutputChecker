

import cv2
import math
import numpy as np
import matplotlib.pyplot as plt


def apply_angular_wave(image, amplitude, frequency):
    height, width = image.shape[:2]
    
    # Generate coordinate grid
    y,x = np.mgrid[0:height, 0:width]
    
    # Compute angle based on coordinates
    angle = np.arctan2(y - height/2, x - width/2)
    
    # Compute displacement based on angle
    displacement = amplitude * np.sin(frequency * angle)
    
    # Apply displacement to coordinates
    x_displaced = x + displacement * np.cos(angle)
    y_displaced = y + displacement * np.sin(angle)
    
    # Interpolate pixel values based on new coordinates
    output = cv2.remap(image, x_displaced.astype(np.float32), y_displaced.astype(np.float32),
                       interpolation=cv2.INTER_LINEAR)
    
    return output

# Load image
image =  cv2.imread(r"C:\Users\WIN\Downloads\homo.jpg",0)

# Apply angular wave effect
amplitude = 30  # Adjust the amplitude of the wave
frequency = 5  # Adjust the frequency of the wave
result = apply_angular_wave(image, amplitude, frequency)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
