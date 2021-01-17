import random


def gnom(lst):
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


m = 5

lst = [random.randint(1, 100) for _ in range(2 * m + 1)]

print(gnom(lst))
print(lst[len(lst) // 2])
