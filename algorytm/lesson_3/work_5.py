# 5.В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

MIN_ELEM = MAX_ITEM
IDX = 0

for i in array:
    if i < 0:
        if abs(i) < abs(MIN_ELEM):
            MIN_ELEM = i
            idx_min_elem = IDX
    IDX += 1


print(f'Максимальный отрицательный элемент в массиве: {MIN_ELEM}, его позиция: {idx_min_elem}')
