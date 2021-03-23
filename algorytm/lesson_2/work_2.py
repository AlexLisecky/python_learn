# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# решение через цикл
a = int(input('Введите натурально число: '))
even = 0
noteven = 0
while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        noteven += 1
    a = a // 10
print(f'четных цифр = {even} , нечетных цифр = {noteven}')


# решение через рекурсию
def evenfunc(a, even, noteven):
    if a == 0:
        return even, noteven
    if a % 2 == 0:
        even += 1
        return evenfunc(a // 10, even, noteven)
    else :
        noteven += 1
        return evenfunc(a // 10, even, noteven)


print(evenfunc(int(input('Введите натурально число: ')), 0, 0))
