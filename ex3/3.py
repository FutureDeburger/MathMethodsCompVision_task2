import cv2 as cv

my_image = cv.imread('3a.jpg')


# a
a1 = cv.GaussianBlur(my_image,(9, 9), 1)
a2 = cv.GaussianBlur(my_image,(9, 9), 4)
a3 = cv.GaussianBlur(my_image,(9, 9), 6)
# cv.imshow("a1", a1)
# cv.imshow("a2", a2)
# cv.imshow("a3", a3)


# b
b1 = cv.GaussianBlur(my_image,(0, 0), 1)
b2 = cv.GaussianBlur(my_image,(0, 0), 4)
b3 = cv.GaussianBlur(my_image,(0, 0), 6)
# cv.imshow("b1", b1)
# cv.imshow("b2", b2)
# cv.imshow("b3", b3)


# c
c1 = cv.GaussianBlur(my_image, (0, 0), sigmaX=1, sigmaY=9)
# cv.imshow("c1", c1)


# d
d1 = cv.GaussianBlur(my_image, (0, 0), sigmaX=9, sigmaY=1)
# cv.imshow("d1", d1)


# e
e1 = cv.GaussianBlur(c1, (0, 0), sigmaX=9, sigmaY=1)
# cv.imshow("e1", e1)


# f
f1 = cv.GaussianBlur(my_image, (9, 9), sigmaX=0, sigmaY=0)
# cv.imshow("f1", f1)


cv.waitKey(0)
cv.destroyAllWindows()