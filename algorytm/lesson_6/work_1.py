#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

#● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

#● написать 3 варианта кода (один у вас уже есть);

#● проанализировать 3 варианта и выбрать оптимальный;

#● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

#● написать общий вывод: какой из трёх вариантов лучше и почему.



import random
import sys


def Calc_memory(*args):  # функция для подсчета памяти переменных
    total = 0
    for i in args:
        total += sys.getsizeof(i)
    total += sys.getsizeof(total)
    print(f'Количество памяти: {total}')


def funk_for(n):
    array_idx_FOR = []
    idx = 0
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    for i in array:
        if i % 2 == 0:
            array_idx_FOR.append(idx)
        idx += 1

    Calc_memory(array_idx_FOR, idx, MIN_ITEM, MAX_ITEM, array)

    return array_idx_FOR


def funk_enumerate(n):
    array_idx_ENUMERATE = []
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    for i, item in enumerate(array):
        if item % 2 == 0:
            array_idx_ENUMERATE.append(i)
    Calc_memory(array_idx_ENUMERATE, MIN_ITEM, MAX_ITEM, array)

    return array_idx_ENUMERATE


def funk_while(n):
    array_idx_WHILE = []
    idx = 0
    i = 0
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    while n > 0:
        if array[i] % 2 == 0:
            array_idx_WHILE.append(idx)
        i += 1
        idx += 1
        n -= 1
    Calc_memory(array_idx_WHILE, idx, i, MIN_ITEM, MAX_ITEM, array, n)

    return array_idx_WHILE


print(f'Индексы четных элементов: {funk_for(10)}')
print(f'Индексы четных элементов: {funk_enumerate(10)}')
print(f'Индексы четных элементов: {funk_while(10)}')

#Количество памяти: 190
#Индексы четных элементов: [5, 8]
#Количество памяти: 176
#Индексы четных элементов: [2, 3]
#Количество памяти: 216
#Индексы четных элементов: [0, 9]

# В большистве случаев выполнение через цикл while забирало больше всего памяти, а через функцию
# enumerate меньше всего.


# Имя ОС	Майкрософт Windows 10 Pro
# Версия	10.0.18363 Сборка 18363
# Тип	Компьютер на базе x64

# Python 3.8.4 