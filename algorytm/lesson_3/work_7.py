# 7.В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = [10, 9, 8, 7, 6, 5, 5]
print(array)
min_number = MAX_ITEM
double_min_number = MAX_ITEM

for i in array:
    if i == min_number:
        double_min_number = min_number
    if i < min_number:
        min_number = i

for i in array:
    if min_number != i:
        if i < double_min_number:
            double_min_number = i

print(min_number, double_min_number)
