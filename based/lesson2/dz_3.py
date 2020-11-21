# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
print('Вариант решения задачи через список')
number_mounth = int(input('Введите номер месяца от 1 до 12: '))
while True:
    if 0 < number_mounth < 13:
        break
    else:
        number_mounth = int(input('Введите номер месяца от 1 до 12: '))
list_year = ['Зима', 'Весна', 'Лето', 'Осень']
if number_mounth == 12 or number_mounth == 1 or number_mounth == 2:
    print(f'Введенный месяц относится к {list_year[0]}')
elif number_mounth == 3 or number_mounth == 4 or number_mounth == 5:
    print(f'Введенный месяц относится к {list_year[1]}')
elif number_mounth == 6 or number_mounth == 7 or number_mounth == 8:
    print(f'Введенный месяц относится к {list_year[2]}')
else:
    print(f'Введенный месяц относится к {list_year[3]}')

print('Вариант решения задачи через словарь')
number_mounth = int(input('Введите номер месяца от 1 до 12: '))
while True:
    if 0 < number_mounth < 13:
        break
    else:
        number_mounth = int(input('Введите номер месяца от 1 до 12: '))
dict_year = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if number_mounth == 12 or number_mounth == 1 or number_mounth == 2:
    print(f'Введенный месяц относится к {dict_year.get(1)}')
elif number_mounth == 3 or number_mounth == 4 or number_mounth == 5:
    print(f'Введенный месяц относится к {dict_year.get(2)}')
elif number_mounth == 6 or number_mounth == 7 or number_mounth == 8:
    print(f'Введенный месяц относится к {dict_year.get(3)}')
else:
    print(f'Введенный месяц относится к {dict_year.get(4)}')
