import cv2 as cv


image = cv.imread('13.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow('Original Image', image)
# cv.imshow('Gray Image', image_gray)


thresh_value = 128

ret, thresh_binary = cv.threshold(image, thresh_value, 255, cv.THRESH_BINARY)
ret, thresh_binary_inv = cv.threshold(image, thresh_value, 255, cv.THRESH_BINARY_INV)
ret, thresh_trunc = cv.threshold(image, thresh_value, 255, cv.THRESH_TRUNC)
ret, thresh_tozero = cv.threshold(image, thresh_value, 255, cv.THRESH_TOZERO)
ret, thresh_tozero_inv = cv.threshold(image, thresh_value, 255, cv.THRESH_TOZERO_INV)

cv.imshow('THRESH_BINARY', thresh_binary)
cv.imshow('THRESH_BINARY_INV', thresh_binary_inv)
cv.imshow('THRESH_TRUNC', thresh_trunc)
cv.imshow('THRESH_TOZERO', thresh_tozero)
cv.imshow('THRESH_TOZERO_INV', thresh_tozero_inv)

cv.waitKey(0)
cv.destroyAllWindows()


# a
# adaptive_mean_5 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
# adaptive_gaussian_5 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)
#
# cv.imshow('Adaptive Mean C=5', adaptive_mean_5)
# cv.imshow('Adaptive Gaussian C=5', adaptive_gaussian_5)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


# b

# # C = 0
# adaptive_mean_0 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
# adaptive_gaussian_0 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
#
# # C = -5
# adaptive_mean_minus5 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, -5)
# adaptive_gaussian_minus5 = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, -5)
#
#
# cv.imshow('Adaptive Mean C=0', adaptive_mean_0)
# cv.imshow('Adaptive Gaussian C=0', adaptive_gaussian_0)
# cv.imshow('Adaptive Mean C=-5', adaptive_mean_minus5)
# cv.imshow('Adaptive Gaussian C=-5', adaptive_gaussian_minus5)
#
# cv.waitKey(0)
# cv.destroyAllWindows()