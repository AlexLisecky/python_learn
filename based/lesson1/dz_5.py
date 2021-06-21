money = int(input("Введите количество выручки: "))
trouble = int(input("Введите количество издержек: "))
if money > trouble:
    print("Фирма работает в прибыль")
    rent = money / trouble
    print(f"Рентабельность фирмы составляет {rent:.2f}")
    people = int(input("Укажите количество работников фирмы: "))
    people_rent = money / people
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {people_rent:.2f}.")
else:
    print("Фирма работает в убыток")
