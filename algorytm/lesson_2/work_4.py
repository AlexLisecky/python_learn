# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# решение через цикл
n = int(input('Введите длину последовательности: '))
a = 1
summ = 0
while n > 0:
    print(a)
    summ += a
    if a > 0:
        a = -(a / 2)
    else:
        a = abs(a / 2)
    n = n - 1
print(f'Cумма = {summ}')


# решение через рекурсию
def func(n, a, summ):
    if n == 1:
        return (f'Сумма = {summ}')
    if a > 0:
        a = -(a / 2)
        summ += a
        return func(n - 1, a, summ)
    else:
        a = abs(a / 2)
        summ += a
        return func(n - 1, a, summ)


print(func(int(input('Введите длину последовательности: ')), 1, 1))
