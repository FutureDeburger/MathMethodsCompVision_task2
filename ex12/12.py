import cv2 as cv


my_image = cv.imread('12a.jpg')
cv.imshow('Image', my_image)


# a
resized_image_1 = cv.resize(my_image, None, fx=0.5, fy=0.5)
resized_image_2 = cv.resize(resized_image_1, None, fx=0.5, fy=0.5)
resized_image_3 = cv.resize(resized_image_2, None, fx=0.5, fy=0.5)
cv.imshow('Resized Image', resized_image_3)


# b
pyrdown_image_1 = cv.pyrDown(my_image)
pyrdown_image_2 = cv.pyrDown(pyrdown_image_1)
pyrdown_image_3 = cv.pyrDown(pyrdown_image_2)
cv.imshow('Pyrdown Image', pyrdown_image_3)


cv.waitKey(0)
cv.destroyAllWindows()