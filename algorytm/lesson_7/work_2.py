# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def make_lst(SIZE):
    array = []

    while SIZE > 0:
        spam = round(random.random() * 100 - 50, 3)
        if spam > 0:
            array.append(spam)
            SIZE -= 1
    return array


def merge_list(left_lst, right_lst):
    lst = []
    i = j = 0

    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] < right_lst[j]:
            lst.append(left_lst[i])
            i += 1
        else:
            lst.append(right_lst[j])
            j += 1
    if i < len(left_lst):
        lst += left_lst[i:]
    if j < len(right_lst):
        lst += right_lst[j:]

    return lst


def merge(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2

    left = merge(lst[:mid])
    right = merge(lst[mid:])
    return merge_list(left, right)


lst = make_lst(10)

print(lst)
print(merge(lst))
