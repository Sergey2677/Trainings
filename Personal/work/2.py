# 2. Пользователь вводит дату в формате ДД.ММ.ГГГГ. Вывести первый день месяца, последний день месяца, сам месяц.

import calendar

# Словари
days = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}
month = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}

# Пользователь вводит дату в формате ДД.ММ.ГГГГ
# В блок обернул так как пользователь может ввести некорректную дату
try:
    input_date = tuple(map(int, input('Введите дату в формате ДД.ММ.ГГГГ: ').split('.')))
    first_number, last_number = calendar.monthrange(input_date[2], input_date[1])
    first_day = calendar.weekday(input_date[2], input_date[1], first_number)
    last_day = calendar.weekday(input_date[2], input_date[1], last_number)
except:
    raise ValueError('Некорректно введена дата, требуемый формат: ДД.ММ.ГГГГ')

print(f'Первый день месяца: {first_number} число - {days[first_day]}')
print(f'Последний день месяца: {last_number} число - {days[last_day]}')
print(f'Месяц: {month[input_date[1]]}')
