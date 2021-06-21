user_time = int(input("Введите время в секундах: "))
hours = (user_time // 3600) % 24
minutes = (user_time // 60) % 60
second = user_time % 60
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if second < 10:
    second = "0" + str(second)
print(f"Время на текущий момент {hours}:{minutes}:{second}.")
