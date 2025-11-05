import cv2 as cv
import numpy as np


image = cv.imread('14.jpg')
cv.imshow('Original Image', image)


# 1. Находим основные границы с помощью детектора границ Canny
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)

# 2. Сегментируем изображение с помощью pyrMeanShiftFiltering
segmented = cv.pyrMeanShiftFiltering(image, sp=20, sr=40, maxLevel=2)

# 3. Сглаживаем каждую часть отдельно (применяем размытие к сегментированному изображению)
smoothed = cv.medianBlur(segmented, 7)

# 4. Альфа-смешение: объединяем сглаженные области с границами
# Создаем маску границ (расширяем для лучшего покрытия)
kernel = np.ones((3, 3), np.uint8)
edges_dilated = cv.dilate(edges, kernel, iterations=1)

# Нормализуем маску для альфа-смешения
alpha_mask = edges_dilated.astype(np.float32) / 255.0

# Применяем альфа-смешение: где границы - оригинальное изображение, где нет - сглаженное
result = np.zeros_like(image, dtype=np.float32)
for i in range(3):
    result[:, :, i] = (image[:, :, i].astype(np.float32) * alpha_mask + smoothed[:, :, i].astype(np.float32) * (1 - alpha_mask))
result = result.astype(np.uint8)


cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()