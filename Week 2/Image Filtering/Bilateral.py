#highly effective in noise removal while keeping edges sharp

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('C:/Users/pavan\Downloads/R.png')
assert img is not None, "file could not be read, check with os.path.exists()"
blur = cv.bilateralFilter(img,101,101,101) # number should be odd
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()