import cv2 as cv
import numpy as np


image = cv.imread('15.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Ядро для выделения линий под углом 60°
kernel = np.array([
    [-1, -1,  0,  1,  1],
    [-1, -1,  0,  1,  1],
    [-1, -1,  0,  1,  1],
    [-1, -1,  0,  1,  1],
    [-1, -1,  0,  1,  1]], dtype=np.float32)

filtered = cv.filter2D(gray, ddepth=-1, kernel=kernel)

cv.imshow("Original", image)
cv.imshow("Lines at 60 degrees", filtered)

cv.waitKey(0)
cv.destroyAllWindows()