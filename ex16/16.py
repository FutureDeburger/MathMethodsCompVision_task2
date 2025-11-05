import cv2 as cv
import numpy as np


image = cv.imread('16.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# a
kernel_3x3 = np.array([
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]], dtype=np.float32)

# Якорь в центре по умолчанию — (1,1) для 3x3, но filter2D сам это учитывает.
filtered_full = cv.filter2D(gray, ddepth=-1, kernel=kernel_3x3, borderType=cv.BORDER_DEFAULT)


# --- b) Два одномерных ядра (строка и столбец) ---
# В задании строка и столбец одинаковые: (1/4, 2/4, 1/4)
kernel_1d = np.array([1/4, 2/4, 1/4], dtype=np.float32)   # 1×3
kernel_1d_col = kernel_1d.reshape(3, 1)                    # 3×1

# Применяем фильтр дважды через filter2D
intermediate = cv.filter2D(gray, ddepth=-1, kernel=kernel_1d.reshape(1,3), borderType=cv.BORDER_DEFAULT)
filtered_sep = cv.filter2D(intermediate, ddepth=-1, kernel=kernel_1d_col, borderType=cv.BORDER_DEFAULT)

# Для контроля можно также использовать cv.sepFilter2D (внутри делает то же самое)
filtered_sep_alt = cv.sepFilter2D(gray, ddepth=-1, kernelX=kernel_1d, kernelY=kernel_1d)


cv.imshow('Original Gray', gray)
cv.imshow('Gaussian 3x3 (filter2D)', filtered_full)
cv.imshow('Separable: horiz then vert (filter2D twice)', filtered_sep)
cv.imshow('Separable using sepFilter2D (control)', filtered_sep_alt)


cv.waitKey(0)
cv.destroyAllWindows()