# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_number = 0
min_number = MAX_ITEM


for i in array:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i

print(max_number)
print(min_number)

min_idx = array.index(min_number)
max_idx = array.index(max_number)



array[min_idx],array[max_idx] = array[max_idx],array[min_idx]
print(array)
