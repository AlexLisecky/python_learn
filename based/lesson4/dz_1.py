from sys import argv

file_name, work_hour, pay, premi = argv

result = int(work_hour) * int(pay) + int(premi)
print(f'Заработная плата сотрудника: {result}')

# (venv) D:\project\lesson4>python dz_1.py 100 200 300
# Заработная плата сотрудника: 20300
