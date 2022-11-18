# 5. Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Пользователь
# вводит третью дату в формате ДД.ММ.ГГГГ ЧЧ:ММ. Определить, лежит ли дата
# внутри временного интервала, образованного первыми двумя датами.

import datetime

# 10.04.1997 10:11
input_date, input_time = input("Дата(1) Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ").split()
input_date2, input_time2 = input("Дата (2) Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ").split()
input_date3, input_time3 = input("Дата (3) Введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ: ").split()


# Сначала формируем список в котором будут находится значения даты в виде int, затем реверсируем список с датой,
# так как в при создании класса datetime нам нужно подавать данные в
# обратном порядке, в последовательности: year, month, day, hour, minute, second, microsecond.
# И создаем два объекта
dt = datetime.datetime(*reversed(list(map(int, input_date.split('.')))), *map(int, input_time.split(':')))
dt2 = datetime.datetime(*reversed(list(map(int, input_date2.split('.')))), *map(int, input_time2.split(':')))
dt3 = datetime.datetime(*reversed(list(map(int, input_date3.split('.')))), *map(int, input_time3.split(':')))

print('Дата (3) входит в интервал между датой (1) и датой (2)' if dt < dt3 < dt2 or dt == dt3 or dt2 == dt3 else 'Дата (3) не входит в интервал между датой (1) и датой (2)')