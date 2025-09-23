import cv2 as cv
import numpy as np

my_image = np.zeros((100, 100), dtype=np.uint8)
my_image[50, 50] = 255

# a
blurred_5x5 = cv.GaussianBlur(my_image,(5, 5), 0)

# b
blurred_9x9 = cv.GaussianBlur(my_image,(9, 9), 0)

# c
double_blurred_5x5 = cv.GaussianBlur(blurred_5x5, (5, 5), 0)


cv.imshow("5x5 Gaussian", blurred_5x5)
cv.imshow("9x9 Gaussian", blurred_9x9)
cv.imshow("5x5 Gaussian Double", double_blurred_5x5)


cv.waitKey(0)
cv.destroyAllWindows()