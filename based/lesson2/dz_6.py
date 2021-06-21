goods = []
while True:
    answer = input('Введите "Да" если хотите внести товар в список: ')
    if answer.lower() == 'да':
        number_goods = int(input('Введите номер товара: '))
        parametr = {}
        while True:
            answer = input('Введите "Да" если хотите внести в категорию товары параметры: ')
            if answer.lower() == 'да':
                parametr_key = input("Введите параметр товара: ")
                parametr_value = input("Введите пояснение для товара: ")
                parametr[parametr_key] = parametr_value
            else:
                break
        goods.append(tuple([number_goods, parametr]))
    else:
        break
print(goods)

analitick = {}
for i in goods:
    for parametr_key,parametr_value in i[1].items():
        if parametr_key in analitick:
            analitick[parametr_key].append(parametr_value)
        else:
            analitick[parametr_key] = [parametr_value]
print(analitick)