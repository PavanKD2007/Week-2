#takes the median of all the pixels under the kernel area and the central element is replaced with this median value.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('C:/Users/pavan\Downloads/R.png')
assert img is not None, "file could not be read, check with os.path.exists()"
median = cv.medianBlur(img,101) # odd number
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()