import cv2 as cv

my_image = cv.imread('1a.jpeg')

# a
blurred_3x3 = cv.GaussianBlur(my_image, (3, 3), 0)
blurred_5x5 = cv.GaussianBlur(my_image, (5, 5), 0)
blurred_9x9 = cv.GaussianBlur(my_image, (9, 9), 0)
blurred_11x11 = cv.GaussianBlur(my_image, (11, 11), 0)

cv.imshow("Original", my_image)
cv.imshow("3x3 Gaussian", blurred_3x3)
cv.imshow("5x5 Gaussian", blurred_5x5)
cv.imshow("9x9 Gaussian", blurred_9x9)
cv.imshow("11x11 Gaussian", blurred_11x11)


# b
double_blurred_5x5 = cv.GaussianBlur(blurred_5x5, (5, 5), 0)
cv.imshow("5x5 Gaussian Double", double_blurred_5x5)


cv.waitKey(0)
cv.destroyAllWindows()