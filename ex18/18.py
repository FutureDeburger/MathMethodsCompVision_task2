import cv2 as cv
import numpy as np


img = cv.imread('18.png', cv.IMREAD_GRAYSCALE)

# --- 3×3 Собель и Лапласиан ---
sobel_x_3 = np.array([[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]], dtype=np.float32)

sobel_y_3 = np.array([[-1, -2, -1],
                      [ 0,  0,  0],
                      [ 1,  2,  1]], dtype=np.float32)

laplacian_3 = np.array([[ 0,  1,  0],
                        [ 1, -4,  1],
                        [ 0,  1,  0]], dtype=np.float32)

# Первая производная (градиенты по X и Y)
grad_x_3 = cv.filter2D(img, cv.CV_64F, sobel_x_3)
grad_y_3 = cv.filter2D(img, cv.CV_64F, sobel_y_3)
grad_3 = cv.magnitude(grad_x_3, grad_y_3)

# Вторая производная (лапласиан)
lap_3 = cv.filter2D(img, cv.CV_64F, laplacian_3)

# --- Увеличиваем размер ядра: 5×5, 9×9, 13×13 ---
# Используем встроенный Sobel и Laplacian, потому что самим писать ядра большого размера — мазохизм
for k in [5, 9, 13]:
    sobel_large = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=k)
    lap_large = cv.Laplacian(img, cv.CV_64F, ksize=k)

    cv.imshow(f'Sobel (k={k})', sobel_large)
    cv.imshow(f'Laplacian (k={k})', lap_large)

# Показываем базовые 3x3
cv.imshow('Original', img)
cv.imshow('Sobel magnitude (3x3)', grad_3)
cv.imshow('Laplacian (3x3)', lap_3)

cv.waitKey(0)
cv.destroyAllWindows()
