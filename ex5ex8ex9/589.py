import cv2 as cv
import numpy as np

src1 = cv.imread('src1.jpg')
src2 = cv.imread('src2.jpg')


grayscale_src1 = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
grayscale_src2 = cv.cvtColor(src2, cv.COLOR_BGR2GRAY)

# cv.imshow("grayscale_src1", grayscale_src1)
# cv.imshow("grayscale_src2", grayscale_src2)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


# a
diff12 = cv.absdiff(grayscale_src1, grayscale_src2)
cv.imshow("diff12", diff12)


# b
retval, binary_diff_image = cv.threshold(diff12, 30, 255, cv.THRESH_BINARY)
cv.imshow("binary_diff_image", binary_diff_image)


# c
# kernel = cv.getStructuringElement(cv.MORPH_RECT,(5, 5))
without_noise_binary_diff_image = cv.morphologyEx(binary_diff_image, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5, 5)))
cv.imshow("without_noise_binary_diff_image", without_noise_binary_diff_image)


# d
erode_without_noise_binary_diff_image = cv.erode(without_noise_binary_diff_image, cv.getStructuringElement(cv.MORPH_RECT,(5, 5)))
result = cv.bitwise_xor(without_noise_binary_diff_image, erode_without_noise_binary_diff_image)
cv.imshow("result", result)


# 8
def keep_largest_component(mask):

    num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(mask, connectivity=8)

    if num_labels <= 1:
        return mask

    largest_label = np.argmax(stats[1:, cv.CC_STAT_AREA]) + 1
    largest_area = stats[largest_label, cv.CC_STAT_AREA]

    # print(f"Найдено компонент: {num_labels}")
    # print(f"Самая большая компонента: метка {largest_label}, площадь {largest_area} пикселей")

    cleaned_mask = np.zeros_like(mask)
    cleaned_mask[labels == largest_label] = 255

    return cleaned_mask

largest_component_mask = keep_largest_component(without_noise_binary_diff_image)
cv.imshow("largest_component_mask", largest_component_mask)

largest_contour_mask = keep_largest_component(result)
cv.imshow("largest_contour_mask", largest_contour_mask)


# 9
src3 = cv.imread('for9ex.jpg')
mask_from_8 = largest_component_mask
mask_resized = cv.resize(mask_from_8, (src3.shape[1], src3.shape[0]))
colored_cup = np.zeros_like(src3)
colored_cup[mask_resized == 255] = [0, 0, 0]
res = src3.copy()
cv.copyTo(colored_cup, mask_resized, res)
cv.imshow("res", res)

cv.waitKey(0)
cv.destroyAllWindows()