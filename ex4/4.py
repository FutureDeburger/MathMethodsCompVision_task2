import cv2 as cv

src1 = cv.imread('src1.jpg')
src2 = cv.imread('src2.jpg')


# a
diff12 = cv.absdiff(src1, src2)
cv.imshow("diff12", diff12)


# b
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5, 5))
eroded_image = cv.erode(diff12, kernel)
dilated_image = cv.dilate(eroded_image, kernel)
cleandiff = dilated_image
cv.imshow("cleandiff", cleandiff)


# c
dilated_image = cv.dilate(diff12, kernel)
eroded_image = cv.erode(dilated_image, kernel)
dirtydiff = eroded_image
cv.imshow("dirtydiff", dirtydiff)



cv.waitKey(0)
cv.destroyAllWindows()