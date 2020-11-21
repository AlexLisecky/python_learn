number = int(input("Введите целое положительное число: "))
max = 0
while number > 0:
    last = number % 10
    number = number // 10
    if last > max:
        max = last
print(max)
