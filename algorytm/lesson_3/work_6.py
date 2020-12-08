# 6.В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
SUMM = 0

print(array)

max_number = 0
min_number = MAX_ITEM

for i in array:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i

print(f'Максимальное число: {max_number}')
print(f'Минимальное число: {min_number}')

min_idx = array.index(min_number)
max_idx = array.index(max_number)

print(f'Индекс минимального числа: {min_idx}')

print(f'Индекс максимального числа: {max_idx}')

if min_idx > max_idx:
    min_idx,max_idx = max_idx,min_idx

for i in range(min_idx + 1, max_idx):
    SUMM += array[i]

print(f'Сумма элементов между максимальным и минимальным числом: {SUMM}')