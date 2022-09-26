# Вводятся названия городов в одну строку через пробел.
# На их основе формируется кортеж. Если в этом кортеже присутствует город "Ульяновск", то этот элемент следует удалить (создав новый кортеж).
# Результат вывести на экран в виде строки с названиями городов через пробел.
# Sample Input:
# Воронеж Самара Тольятти Ульяновск Пермь
# Sample Output:
# Воронеж Самара Тольятти Пермь

# put your python code here

t = tuple(input().split())

if t.count('Ульяновск') > 0:
    t = tuple(i for i in t if i != 'Ульяновск')

print(*t)
