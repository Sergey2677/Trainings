# Вводятся названия городов в одну строку через пробел.
# На их основе формируется кортеж. Если в этом кортеже нет города "Москва", то следует его добавить в конец кортежа.
# Результат вывести на экран в виде строки с названиями городов через пробел.
# Sample Input:
# Уфа Казань Самара
# Sample Output:
# Уфа Казань Самара Москва

# put your python code here

t = tuple(input().split())

if t.count('Москва') == 0:
    t += ('Москва', )

print(*t)