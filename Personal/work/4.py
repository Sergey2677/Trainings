# Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Вывести разницу между датами в часах, днях (целых), минутах и секундах.

import datetime

# 10.04.1997 10:11
input_date, input_time = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ").split()
input_date2, input_time2 = input("Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ").split()

# Сначала формируем список в котором будут находится значения даты в виде int, затем реверсируем список с датой,
# так как в при создании класса datetime нам нужно подавать данные в
# обратном порядке, в последовательности: year, month, day, hour, minute, second, microsecond.
# И создаем два объекта
dt = datetime.datetime(*reversed(list(map(int, input_date.split('.')))), *map(int, input_time.split(':')))
dt2 = datetime.datetime(*reversed(list(map(int, input_date2.split('.')))), *map(int, input_time2.split(':')))

print(dt - dt2 if dt > dt2 else dt2 - dt)
