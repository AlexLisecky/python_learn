# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

numbers = range(20, 241)
result = [el for el in numbers if el % 20 == 0 or el % 21 == 0]
print(result)
