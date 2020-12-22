# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict, deque
#                   0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16
# Шестнадцатеричные	0	1	2	3	4	5	6	7	8	9	a	b	c	d	e	f	10

# 1F5 = 1×16**2 + F×16**1 + 5×16**0 = 162 + 15×16 + 5 = 501.

# FF = F×16**1 + F×16**0 = 15×16**1 + 15×16**0 = 15×16 + 15 = 255.

# 1375 = 1000 + 300 +70 + 5 = 1×10**3 + 3×10**2 + 7×10**1 + 5×10**0.

# 136 = 100 + 30 + 6 = 1×10**2 + 3×10**1 + 6×10**0.


def string_to_number(string):
    number = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        number += system_16[num[i]] * 16 ** i
    return number


def number_to_string(numb):
    num = deque()
    while numb > 0:
        a = numb % 16
        for i in system_16:
            if system_16[i] == a:
                num.append(i)
        numb = numb // 16
    num.reverse()
    return list(num)


system = '0123456789ABCDEF'
system_16 = defaultdict(int)
counter = 0

for key in system:
    system_16[key] += counter
    counter += 1

num_1 = string_to_number(input('Введите первое число: ').upper())
num_2 = string_to_number(input('Введите второе число: ').upper())

# num_1= string_to_number('A2')
# num_2= string_to_number('C4F')

print(f'Сумма чисел: {number_to_string(num_1 + num_2)}')
print(f'Произведение чисел: {number_to_string(num_1 * num_2)}')
