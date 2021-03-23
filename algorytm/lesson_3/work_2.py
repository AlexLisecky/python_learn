# 2.Во втором массиве сохранить индексы четных элементов первого массива. Например,
# если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random
idx = 0
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


array_idx = []

for i in array:
    if i % 2 == 0:
        array_idx.append(i - i + idx)
    idx += 1


print(f'Индексы четных элементов: {array_idx}')