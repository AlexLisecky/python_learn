# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import deque, defaultdict

count_enterprise = int(input("Введите количеcтво предприятий: "))
all_profit_enterprise = deque()
profit = deque()
name_enterprise = defaultdict()
loser = []
winner = []

for i in range(count_enterprise):
    quart = 4
    q_count = 1
    name = (input('Введите название предприятия: '))

    while quart > 0:
        profit.append(float(input(f'Введите прибыль за {q_count} квартал предприятия {name}: ')))
        q_count += 1
        quart -= 1
        name_enterprise[name] = sum(profit)

    all_profit_enterprise += profit
    profit.clear()

all_sum = sum(all_profit_enterprise)
avg_sum = all_sum / count_enterprise

for i, item in name_enterprise.items():
    if item > avg_sum:
        winner.append(i)
    else:
        loser.append(i)

print(f'Общая прибыль всех предприятий = {all_sum}')
print(f'Средняя прибыль всех предприятий за год = {avg_sum}')
print(f'Предприятия у которых прибыль выше среднего: {winner}')
print(f'Предприятия у которых прибыль ниже среднего: {loser}')
