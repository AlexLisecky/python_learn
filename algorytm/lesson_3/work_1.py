# 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9


MIN_ITEM = 2
MAX_ITEM = 100
MIN_DIAP = 2
MAX_DIAP = 9  # максимальный и минимальный диапазоны
array = []

for i in range(MIN_ITEM, MAX_ITEM):
    array.append(i)
print(array)

a = [0] * 8
print(a)

for number in array:
    for deli in range(MIN_DIAP, MAX_DIAP):
        if number % deli == 0:
            a[deli - 2] += 1
print(f'{a}')
